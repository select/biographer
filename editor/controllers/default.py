from gluon.contrib import simplejson


def index():
    check_first_user()
    response.files.append(URL(request.application, 'static/biographer-editor/css', 'visualization-html.css'))
    response.files.append(URL(request.application, 'static/biographer-editor/css', 'visualization-svg.css'))
    response.files.append(URL(request.application, 'static/biographer-editor/css', 'jquery-ui-1.8.13.css'))
    #response.files.append(URL(request.application, 'static/js', 'jquery.simulate.js'))  #FIXME why was this imported?
    response.files.append(URL(request.application, 'static/biographer-editor/js', 'jquery-ui-1.8.15.custom.min.js'))
    response.files.append(URL(request.application, 'static/biographer-editor/js', 'jquery.simplemodal.1.4.1.min.js'))
    response.files.append(URL(request.application, 'static/biographer-editor/js', 'd3.js'))
    response.files.append(URL(request.application, 'static/biographer-editor/js', 'd3.layout.js'))
    response.files.append(URL(request.application, 'static/biographer-editor/js', 'd3.geom.js'))
    if (request.vars.import_file != None and request.vars.import_file != '') or request.vars.jgraph or request.vars.jsbgn:
        action, graph, json_string = None, None, None
        if request.vars.jgraph or request.vars.jsbgn:
            result = import_file(request.vars.jgraph or request.vars.jsbgn)
        else:
            result = import_file(request.vars.import_file.file.read().strip(), request.vars.import_file.filename)
        if result:
            action, graph, json_string = result
            if action and graph and json_string:
                undoRegister(action, graph, json_string)
        else:
            response.flash = 'failed importing'
    #----------------------------------
    elif request.vars.biomodel_id:
        model_content = biomodel_fetch(request.vars.biomodel_id, suppress_error=True)
        #----------------------------------
        if model_content:
            action, graph, json_string = import_file(model_content, biomodel_id)
            if action and graph and json_string:
                undoRegister(action, graph, json_string)
    return dict()


def debug():
    if session.debug == None:
        session.debug = True
    else:
        session.debug = not session.debug
    redirect(URL('index'))


def reset():
    session.editor_autosave = None
    session.editor_histroy_undo = None
    session.editor_histroy_redo = None
    redirect(URL('index'))

def import_graph():
    action, graph, json_string = None, None, None

    if request.vars.biomodel_id:
        return biomodel_fetch(request.vars.biomodel_id)
    if request.vars.reactome_id:
        #FIXME implement caching
        #model_path = os.path.join(request.folder, 'static', 'data_models')
        #if not os.path.exists(model_path):
        #    os.mkdir(model_path)
        #if request.vars.identifier+'.jsbgn' in os.listdir(model_path) and not request.vars.force:
        #    model_content = open(os.path.join(model_path, biomodel_id+'.xml'), 'r').read()
        #    response.flash = 'Loaded %s from cache.'%biomodel_id
        graph = reactome_id2jsbgn(request.vars.identifier)
        json_string = simplejson.dumps(graph)
        action = 'Imported Reactome Id: %s' % request.vars.identifier
    if action and graph and json_string:
        return undoRegister(action, graph, json_string)
    raise HTTP(500, 'could not import')


def layout():
    response.generic_patterns = ['html', 'json']
    if not request.vars.layout:
        raise HTTP(500, 'not layout algorithm specified')
    #-------------------
    import os
    import subprocess
    #-------------------
    if request.vars.layout == "biographer":
        filename = request.vars.filename or 'tmp'
        if request.vars.jsbgn:
            open(os.path.join(request.folder, "static", "%s.jsbgn" % filename), 'w').write(request.vars.jsbgn)
        infile = os.path.join(request.folder, "static", "%s.bgin" % filename)
        outfile = os.path.join(request.folder, "static", "%s.bgout" % filename)
        open(infile, 'w').write(request.vars.data)
        executable = os.path.join(request.folder, "static", "layout")
        p = subprocess.Popen([executable, infile, outfile], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p.communicate()
        layout_output = open(outfile, 'r').readlines()
        return layout_output

    elif request.vars.layout == 'graphviz':
        import biographer
        reload(biographer)  # TODO remove in production mode
        bioGraph = biographer.Graph()
        bioGraph.importJSON(session.editor_autosave)
        bioGraph.exportGraphviz(folder=os.path.join(request.folder, "static/graphviz"), useCache=True, updateNodeProperties=True)
        #-------------------
        json_string = bioGraph.exportJSON()
        graph = simplejson.loads(json_string)
    action = 'applied automatic biographer layout'
    return undoRegister(action, graph, json_string)
    #-------------------


def autosave():
    session.editor_autosave = request.vars.json


def undo_push():
    session.editor_autosave = request.vars.graph
    #create history
    if session.editor_histroy_undo == None:
        session.editor_histroy_undo = []
    session.editor_histroy_redo = []
    #pop if history is "full"
    if len(session.editor_histroy_undo) >= 100:
        session.editor_histroy_undo.pop(0)
    #add current result to history
    session.editor_histroy_undo.append(dict(action=request.vars.action, graph=simplejson.loads(request.vars.graph)))


def undo():
    response.generic_patterns = ['json']
    if session.editor_histroy_undo:
        item = session.editor_histroy_undo.pop()
        session.editor_histroy_redo.append(item)
    if not session.editor_histroy_undo:
        last_graph = dict(nodes=[], edges=[])
    else:
        last_graph = session.editor_histroy_undo[-1]['graph']
    session.editor_autosave = simplejson.dumps(last_graph)
    return last_graph


def redo():
    if session.editor_histroy_redo:
        response.generic_patterns = ['json']
        item = session.editor_histroy_redo.pop()
        session.editor_histroy_undo.append(item)
        session.editor_autosave = simplejson.dumps(item['graph'])
        return item
    else:
        return {}


def export():
    file_type = False
    def fix_svg(svg_data):
        import re
        import os
        stylesheet_contents = open(os.path.join(request.folder, 'static' , 'biographer-editor', 'css', 'visualization-svg.css'), 'r').read()
        out = re.sub('@import url[^<]*', stylesheet_contents, svg_data)
        return '<?xml version="1.0" encoding="UTF-8"?>\n%s'%out
    if request.vars.format in 'png jpg pdf tiff'.split():
        file_type = request.vars.format
        java = app_config.get('java', 'path')
        import os
        from subprocess import Popen, PIPE
        from shlex import split
        jar = os.path.join(request.folder, "static", "svg-export-0.2.jar")
        applet = java + " -jar " + jar + " -si -so -f " + request.vars.format
        result = Popen(split(applet), stdin=PIPE, stdout=PIPE).communicate(fix_svg(request.vars.svg_data))      # call Ben's Java Exporter Applet
        out = result[0]  # stdout
        if result[1]:
            raise Exception(result[1])
        print "image export errors: ", result[1]  # stderr

    if not file_type:
        return ''
    import gluon.contenttype
    response.headers['Content-Type'] = gluon.contenttype.contenttype("%s" % file_type)
    filename = "%s.%s" % ('graph', file_type)
    response.headers['Content-disposition'] = "attachment; filename=\"%s\"" % filename
    return out


def render():
    in_url = request.args(0) or request.vars.q
    if in_url.startswith('/'):
        in_url = 'http://%s%s' % (request.env.http_host, in_url)
    if in_url:
        try:
            import urllib2
            file_content = _download(in_url)
        except urllib2.HTTPError, e:
            return 'error getting %s: %s' % (in_url, e)
        action, graph, json_string = import_file(file_content, '')#FIXME this should be done now by libSBGN.js!!
        if action and graph and json_string:
            undoRegister(action, graph, json_string)
    response.files.append(URL(request.application, 'static/biographer-editor/css', 'visualization-html.css'))
    response.files.append(URL(request.application, 'static/biographer-editor/css', 'visualization-svg.css'))
    response.files.append(URL(request.application, 'static/biographer-editor/css', 'jquery-ui-1.8.13.css'))
    #response.files.append(URL(request.application, 'static/js', 'jquery.simulate.js'))  #FIXME why was this imported?
    response.files.append(URL(request.application, 'static/biographer-editor/js', 'jquery-ui-1.8.15.custom.min.js'))
    #response.files.append(URL(request.application, 'static/biographer-editor/js', 'jquery.simplemodal.1.4.1.min.js'))
    response.files.append(URL(request.application, 'static/biographer-editor/js', 'd3.js'))
    response.files.append(URL(request.application, 'static/biographer-editor/js', 'd3.layout.js'))
    response.files.append(URL(request.application, 'static/biographer-editor/js', 'd3.geom.js'))
    response.files.append(URL(request.application, 'static/biographer-editor/js', 'biographer-ui.js'))
    response.files.append(URL(request.application, 'static/biographer-editor/js', 'biographer.editor.js'))
    response.files.append(URL(request.application, 'static/biographer-editor/js', 'interact.js'))
    response.files.append(URL(request.application, 'static/biographer-editor/js', 'libSBGN.js'))
    return dict()


def sbgnml_test():
    import os
    test_path = os.path.join(request.folder, 'static', 'test-files')
    items = []
    #for dn in ['PD']:
    for dn in ['PD', 'ER', 'AF']:
        subitems = []
        items.append(H1(dn))
        for fn in os.listdir(os.path.join(test_path, dn)):
            if fn.endswith('.sbgn'):
                if fn == 'mapk_cascade.sbgn':  # FIXME
                    #print sbgnml2jsbgn(open(os.path.join(test_path, dn, fn), 'r').read())
                    continue
                subitems.append(
                        TR(TH(A(fn, _href=URL('render', vars=dict(q=URL(request.application,  'static/test-files/%s' % dn, fn))),  _target="_blank"),  _colspan=2)),
                    )
                subitems.append(
                    TR(
                        TD(IMG(_src=URL(request.application, 'static/test-files/' + dn, fn[:-5] + '.png'), _alt='sbgn image', _style='max-width: 300px')),
                        TD(PRE('%s' % IFRAME(_src=URL('render', vars=dict(q=URL(request.application, 'static/test-files/%s' % dn, fn))), _width="500px", _height="200px", _scrolling="no", _frameBorder="0"))),
                        ),
                    )
                subitems.append(
                    TR(TH(HR(), _colspan=2)),
                    )
        items.append(TABLE(subitems))
        items.append(HR())
    response.files.append(URL(request.application, 'static/js', 'jquery-ui-1.8.15.custom.min.js'))
    return dict(table=TAG[''](items))


def sbml_test():
    import os
    #test_path = os.path.join(request.folder, 'static', 'sbml-test')
    test_path = os.path.join(request.folder, 'static', 'data_models')
    items = []
    #count = 0
    filenames = [fn for fn in os.listdir(test_path) if fn.startswith('BIOMD') and fn.endswith('.xml')]
    filenames.sort()
    for fn in filenames:
        #if count>380:
        #    break
        #count += 1
        #if count<360:
        #    continue
        items.append(
                TR(TH(A(fn, _href=URL('render', vars=dict(q=URL(request.application, 'static/data_models', fn), layout="biographer", filename=fn)), _target="_blank"), _colspan=2)),
            )
        items.append(
            TR(
                #TD(IMG(_src=URL(request.application, 'static/test-files/'+dn, fn[:-5]+'.png'), _alt='sbgn image', _style='max-width: 300px')),
                TD(PRE(
                    '%s' % IFRAME(_src=URL('render', vars=dict(q=URL(request.application, 'static/data_models', fn), layout="biographer")), _width="500px", _height="200px", _scrolling="no", _frameBorder="0"),
                    _class='show_iframe'
                    ), DIV()),
                ),
            )
        items.append(
            TR(TH(HR(), _colspan=2)),
            )
    response.files.append(URL(request.application, 'static/js', 'jquery-ui-1.8.15.custom.min.js'))
    return dict(table=TAG[''](TABLE(items)))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())
