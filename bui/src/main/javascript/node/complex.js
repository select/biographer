(function(bui) {
    var identifier = 'bui.Complex';

    /**
     * @private
     * Function used for the generation of listener identifiers
     * @param {bui.Complex} Complex
     * @return {String} listener identifier
     */
    var listenerIdentifier = function(Complex) {
        return identifier + Complex.id();
    };

    var sizeChanged = function(node, width, height) {
        var cornerRadius = bui.settings.style.complexCornerRadius;

        var pathData = ['M', width / 2, 0,
                        'H', width - cornerRadius,
                        'L', width, cornerRadius,
                        'V', height - cornerRadius,
                        'L', width - cornerRadius, height,
                        'H', cornerRadius,
                        'L', 0, height - cornerRadius,
                        'V', cornerRadius,
                        'L', cornerRadius, 0,
                        'H', width / 2].join(' ');
        
        this._privates(identifier).path.setAttributeNS(null, 'd', pathData);
    };

    /**
     * @private used from the constructor to improve readability
     */
    var initialPaint = function() {
        var container = this.nodeGroup();
        var size = this.size();
        var privates = this._privates(identifier);
        privates.path = document.createElementNS(bui.svgns, 'path');
        sizeChanged.call(this, this, size.width, size.height);
        container.appendChild(privates.path);
    };

    /**
     * @class
     * Class for SBGN complexes.
     *
     * @extends bui.Node
     * @constructor
     */
    bui.Complex = function() {
        bui.Node.apply(this, arguments);

        this.bind(bui.Node.ListenerType.size,
                sizeChanged.createDelegate(this),
                listenerIdentifier(this));

        initialPaint.call(this);

        this.addClass(bui.settings.css.classes.complex);
    };

    bui.Complex.prototype = {
        tableLayout : function(settings) {
            if (settings === undefined) {
                // TODO put in general settings
                settings = {
                    maxColumns : 3,
                    padding : 25
                };
            }

            // the items of the table array represent rows. Row items represent
            // columns
            var table = [[]];

            /**
             * @private
             * Add a node to the table. This is a private utility function for
             * the sake of readability.
             *
             * @param {bui.Node} node The node which should be added
             */
            var addToTable = function(node) {
                var lastRow = table[table.length - 1];

                if (lastRow.length === settings.maxColumns) {
                    lastRow = [];
                    table.push(row);
                }

                lastRow.push(node);
            };

            var children = this.children();
            for (var i = 0; i < children.length; i++) {
                var node = children[i];

                if (node instanceof bui.Complex) {
                    node.tableLayout(settings);
                }

                addToTable(node);
            }

            console.log(table);

            var totalWidth = Number.MIN_VALUE,
                    totalHeight = settings.padding;

            for (var rowId = 0; rowId < table.length; rowId++) {
                var row = table[rowId];

                var totalColumnWidth = settings.padding,
                        highestColumn = Number.MIN_VALUE;

                for (var columnId = 0; columnId < row.length; columnId++) {
                    // each column holds a node, i.e. a bui.Node instance
                    var columnNode = row[columnId];

                    var size = columnNode.size();
                    highestColumn = Math.max(size.height, highestColumn);

                    console.log(totalColumnWidth);
                    columnNode.position(totalColumnWidth, totalHeight);

                    // this probably needs to go to the end of the loop
                    totalColumnWidth += size.width + settings.padding;
                }

                totalHeight += highestColumn + settings.padding;
                totalWidth = Math.max(totalWidth, totalColumnWidth);
            }

            console.log(totalWidth);
            console.log(totalHeight);

            this.size(totalWidth, totalHeight);
        }
    };

    bui.util.setSuperClass(bui.Complex, bui.Node);
})(bui);