# -*- coding: utf-8 -*-

import biographer

def importer():
	return dict()

example = "<?xml version="1.0" encoding="UTF-8"?>
<sbml xmlns="http://www.sbml.org/sbml/level2/version4" metaid="_000000" level="2" version="4">
  <model metaid="_000001" id="EPSP_Edelstein" name="Edelstein1996_EPSP_AChEvent">
    <notes>
      <body xmlns="http://www.w3.org/1999/xhtml">
        <h1>Model of a nicotinic EPSP in a Torpedo electric organ by Edelstein et al (1996)</h1>
        <p>Acetylcholine is not represented explicitely, but by an event that changes the constants of transition from unliganded to liganded.</p>
        <p>This model originates from BioModels Database: A Database of Annotated Published Models (http://www.ebi.ac.uk/biomodels/). It is copyright (c) 2005-2011 The BioModels.net Team.<br/>For more information see the <a href="http://www.ebi.ac.uk/biomodels/legal.html" target="_blank">terms of use</a>.<br/>To cite BioModels Database, please use: <a href="http://www.ncbi.nlm.nih.gov/pubmed/20587024" target="_blank">Li C, Donizelli M, Rodriguez N, Dharuri H, Endler L, Chelliah V, Li L, He E, Henry A, Stefan MI, Snoep JL, Hucka M, Le Novère N, Laibe C (2010) BioModels Database: An enhanced, curated and annotated resource for published quantitative kinetic models. BMC Syst Biol., 4:92.</a>
      </p>
    </body>
  </notes>
  <annotation>
    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
      <rdf:Description rdf:about="#_000001">
        <dc:creator>
          <rdf:Bag>
            <rdf:li rdf:parseType="Resource">
              <vCard:N rdf:parseType="Resource">
                <vCard:Family>Le Novère</vCard:Family>
                <vCard:Given>Nicolas</vCard:Given>
              </vCard:N>
              <vCard:EMAIL>lenov@ebi.ac.uk</vCard:EMAIL>
              <vCard:ORG rdf:parseType="Resource">
                <vCard:Orgname>EMBL-EBI</vCard:Orgname>
              </vCard:ORG>
            </rdf:li>
          </rdf:Bag>
        </dc:creator>
        <dcterms:created rdf:parseType="Resource">
          <dcterms:W3CDTF>2005-02-02T14:56:11Z</dcterms:W3CDTF>
        </dcterms:created>
        <dcterms:modified rdf:parseType="Resource">
          <dcterms:W3CDTF>2010-11-18T15:10:45Z</dcterms:W3CDTF>
        </dcterms:modified>
        <bqmodel:is>
          <rdf:Bag>
            <rdf:li rdf:resource="urn:miriam:biomodels.db:BIOMD0000000001"/>
          </rdf:Bag>
        </bqmodel:is>
        <bqmodel:is>
          <rdf:Bag>
            <rdf:li rdf:resource="urn:miriam:biomodels.db:MODEL6613849442"/>
          </rdf:Bag>
        </bqmodel:is>
        <bqmodel:isDescribedBy>
          <rdf:Bag>
            <rdf:li rdf:resource="urn:miriam:pubmed:8983160"/>
          </rdf:Bag>
        </bqmodel:isDescribedBy>
        <bqbiol:isVersionOf>
          <rdf:Bag>
            <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0007274"/>
            <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0007166"/>
          </rdf:Bag>
        </bqbiol:isVersionOf>
        <bqbiol:is>
          <rdf:Bag>
            <rdf:li rdf:resource="urn:miriam:taxonomy:7787"/>
          </rdf:Bag>
        </bqbiol:is>
      </rdf:Description>
    </rdf:RDF>
  </annotation>
  <listOfCompartments>
    <compartment metaid="_000002" id="comp1" name="compartment1" size="1e-16" sboTerm="SBO:0000290">
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000002">
            <bqbiol:is>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0031594"/>
              </rdf:Bag>
            </bqbiol:is>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
    </compartment>
  </listOfCompartments>
  <listOfSpecies>
    <species metaid="_000003" id="BLL" name="BasalACh2" compartment="comp1" initialAmount="0" sboTerm="SBO:0000297">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>biliganded basal state</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000003">
            <bqbiol:isVersionOf>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:interpro:IPR002394"/>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0005892"/>
              </rdf:Bag>
            </bqbiol:isVersionOf>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
    </species>
    <species metaid="_000004" id="IL" name="IntermediateACh" compartment="comp1" initialAmount="0" sboTerm="SBO:0000297">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>monoliganded intermediate</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000004">
            <bqbiol:isVersionOf>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:interpro:IPR002394"/>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0005892"/>
              </rdf:Bag>
            </bqbiol:isVersionOf>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
    </species>
    <species metaid="_000005" id="AL" name="ActiveACh" compartment="comp1" initialAmount="0" sboTerm="SBO:0000297">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>monoliganded active state</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000005">
            <bqbiol:isVersionOf>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:interpro:IPR002394"/>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0005892"/>
              </rdf:Bag>
            </bqbiol:isVersionOf>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
    </species>
    <species metaid="_000006" id="A" name="Active" compartment="comp1" initialAmount="0" sboTerm="SBO:0000420">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>unkiganded active state</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000006">
            <bqbiol:isVersionOf>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:interpro:IPR002394"/>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0005892"/>
              </rdf:Bag>
            </bqbiol:isVersionOf>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
    </species>
    <species metaid="_000007" id="BL" name="BasalACh" compartment="comp1" initialAmount="0" sboTerm="SBO:0000297">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>monoliganded basal state</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000007">
            <bqbiol:isVersionOf>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:interpro:IPR002394"/>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0005892"/>
              </rdf:Bag>
            </bqbiol:isVersionOf>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
    </species>
    <species metaid="_000008" id="B" name="Basal" compartment="comp1" initialAmount="1.66057788110262e-21" sboTerm="SBO:0000420">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>unliganded basal state</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000008">
            <bqbiol:isVersionOf>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:interpro:IPR002394"/>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0005892"/>
              </rdf:Bag>
            </bqbiol:isVersionOf>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
    </species>
    <species metaid="_000009" id="DLL" name="DesensitisedACh2" compartment="comp1" initialAmount="0" sboTerm="SBO:0000297">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>biliganded desensitised state</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000009">
            <bqbiol:isVersionOf>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:interpro:IPR002394"/>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0005892"/>
              </rdf:Bag>
            </bqbiol:isVersionOf>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
    </species>
    <species metaid="_000010" id="D" name="Desensitised" compartment="comp1" initialAmount="0" sboTerm="SBO:0000420">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>fully desensitised state</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000010">
            <bqbiol:isVersionOf>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:interpro:IPR002394"/>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0005892"/>
              </rdf:Bag>
            </bqbiol:isVersionOf>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
    </species>
    <species metaid="_000011" id="ILL" name="IntermediateACh2" compartment="comp1" initialAmount="0" sboTerm="SBO:0000297">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>biliganded intermediate</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000011">
            <bqbiol:isVersionOf>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:interpro:IPR002394"/>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0005892"/>
              </rdf:Bag>
            </bqbiol:isVersionOf>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
    </species>
    <species metaid="_000012" id="DL" name="DesensitisedACh" compartment="comp1" initialAmount="0" sboTerm="SBO:0000297">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>monoliganded desensitised state</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000012">
            <bqbiol:isVersionOf>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:interpro:IPR002394"/>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0005892"/>
              </rdf:Bag>
            </bqbiol:isVersionOf>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
    </species>
    <species metaid="_000013" id="I" name="Intermediate" compartment="comp1" initialAmount="0" sboTerm="SBO:0000420">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>unliganted intermediate</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000013">
            <bqbiol:isVersionOf>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:interpro:IPR002394"/>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0005892"/>
              </rdf:Bag>
            </bqbiol:isVersionOf>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
    </species>
    <species metaid="_000014" id="ALL" name="ActiveACh2" compartment="comp1" initialAmount="0" sboTerm="SBO:0000297">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>biliganted active state</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000014">
            <bqbiol:isVersionOf>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:interpro:IPR002394"/>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0005892"/>
              </rdf:Bag>
            </bqbiol:isVersionOf>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
    </species>
  </listOfSpecies>
  <listOfParameters>
    <parameter metaid="metaid_0000037" id="kf_0" value="3000" constant="false" sboTerm="SBO:0000035"/>
    <parameter metaid="metaid_0000038" id="kr_0" value="8000" sboTerm="SBO:0000038"/>
    <parameter metaid="metaid_0000039" id="kf_1" value="1500" constant="false" sboTerm="SBO:0000035"/>
    <parameter metaid="metaid_0000040" id="kr_1" value="16000" sboTerm="SBO:0000038"/>
    <parameter metaid="metaid_0000041" id="kf_2" value="30000" sboTerm="SBO:0000035"/>
    <parameter metaid="metaid_0000042" id="kr_2" value="700" sboTerm="SBO:0000038"/>
    <parameter metaid="metaid_0000043" id="kf_3" value="3000" constant="false" sboTerm="SBO:0000035"/>
    <parameter metaid="metaid_0000044" id="kr_3" value="8.64" sboTerm="SBO:0000038"/>
    <parameter metaid="metaid_0000045" id="kf_4" value="1500" constant="false" sboTerm="SBO:0000035"/>
    <parameter metaid="metaid_0000046" id="kr_4" value="17.28" sboTerm="SBO:0000038"/>
    <parameter metaid="metaid_0000047" id="kf_5" value="0.54" sboTerm="SBO:0000035"/>
    <parameter metaid="metaid_0000048" id="kr_5" value="10800" sboTerm="SBO:0000038"/>
    <parameter metaid="metaid_0000049" id="kf_6" value="130" sboTerm="SBO:0000035"/>
    <parameter metaid="metaid_0000050" id="kr_6" value="2740" sboTerm="SBO:0000038"/>
    <parameter metaid="metaid_0000051" id="kf_7" value="3000" constant="false" sboTerm="SBO:0000035"/>
    <parameter metaid="metaid_0000052" id="kr_7" value="4" sboTerm="SBO:0000038"/>
    <parameter metaid="metaid_0000053" id="kf_8" value="1500" constant="false" sboTerm="SBO:0000035"/>
    <parameter metaid="metaid_0000054" id="kr_8" value="8" sboTerm="SBO:0000038"/>
    <parameter metaid="metaid_0000055" id="kf_9" value="19.7" sboTerm="SBO:0000035"/>
    <parameter metaid="metaid_0000056" id="kr_9" value="3.74" sboTerm="SBO:0000038"/>
    <parameter metaid="metaid_0000057" id="kf_10" value="19.85" sboTerm="SBO:0000035"/>
    <parameter metaid="metaid_0000058" id="kr_10" value="1.74" sboTerm="SBO:0000038"/>
    <parameter metaid="metaid_0000059" id="kf_11" value="20" sboTerm="SBO:0000035"/>
    <parameter metaid="metaid_0000060" id="kr_11" value="0.81" sboTerm="SBO:0000038"/>
    <parameter metaid="metaid_0000061" id="kf_12" value="3000" constant="false" sboTerm="SBO:0000035"/>
    <parameter metaid="metaid_0000062" id="kr_12" value="4" sboTerm="SBO:0000038"/>
    <parameter metaid="metaid_0000063" id="kf_13" value="1500" constant="false" sboTerm="SBO:0000035"/>
    <parameter metaid="metaid_0000064" id="kr_13" value="8" sboTerm="SBO:0000038"/>
    <parameter metaid="metaid_0000065" id="kf_14" value="0.05" sboTerm="SBO:0000035"/>
    <parameter metaid="metaid_0000066" id="kr_14" value="0.0012" sboTerm="SBO:0000038"/>
    <parameter metaid="metaid_0000067" id="kf_15" value="0.05" sboTerm="SBO:0000035"/>
    <parameter metaid="metaid_0000068" id="kr_15" value="0.0012" sboTerm="SBO:0000038"/>
    <parameter metaid="metaid_0000069" id="kf_16" value="0.05" sboTerm="SBO:0000035"/>
    <parameter metaid="metaid_0000070" id="kr_16" value="0.0012" sboTerm="SBO:0000038"/>
    <parameter metaid="metaid_0000072" id="t2" value="20"/>
  </listOfParameters>
  <listOfReactions>
    <reaction metaid="_000016" id="React0" name="React0" sboTerm="SBO:0000177">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>first ligand on basal</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000016">
            <bqbiol:is>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0042166"/>
              </rdf:Bag>
            </bqbiol:is>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
      <listOfReactants>
        <speciesReference sboTerm="SBO:0000010" species="B"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference sboTerm="SBO:0000011" species="BL"/>
      </listOfProducts>
      <kineticLaw sboTerm="SBO:0000080">
        <notes>
          <body xmlns="http://www.w3.org/1999/xhtml">
            <p>kf_0 * B - kr_0 * BL</p>
          </body>
        </notes>
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <apply>
            <times/>
            <ci> comp1 </ci>
            <apply>
              <minus/>
              <apply>
                <times/>
                <ci> kf_0 </ci>
                <ci> B </ci>
              </apply>
              <apply>
                <times/>
                <ci> kr_0 </ci>
                <ci> BL </ci>
              </apply>
            </apply>
          </apply>
        </math>
      </kineticLaw>
    </reaction>
    <reaction metaid="_000017" id="React1" name="React1" sboTerm="SBO:0000177">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>second ligand on basal</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000017">
            <bqbiol:is>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0042166"/>
              </rdf:Bag>
            </bqbiol:is>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
      <listOfReactants>
        <speciesReference sboTerm="SBO:0000010" species="BL"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference sboTerm="SBO:0000011" species="BLL"/>
      </listOfProducts>
      <kineticLaw sboTerm="SBO:0000080">
        <notes>
          <body xmlns="http://www.w3.org/1999/xhtml">
            <p>kf_1 * BL - kr_1 * BLL</p>
          </body>
        </notes>
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <apply>
            <times/>
            <ci> comp1 </ci>
            <apply>
              <minus/>
              <apply>
                <times/>
                <ci> kf_1 </ci>
                <ci> BL </ci>
              </apply>
              <apply>
                <times/>
                <ci> kr_1 </ci>
                <ci> BLL </ci>
              </apply>
            </apply>
          </apply>
        </math>
      </kineticLaw>
    </reaction>
    <reaction metaid="_000018" id="React2" name="React2" sboTerm="SBO:0000181">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>opening of biliganded</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000018">
            <bqbiol:is>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0004889"/>
              </rdf:Bag>
            </bqbiol:is>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
      <listOfReactants>
        <speciesReference sboTerm="SBO:0000010" species="BLL"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference sboTerm="SBO:0000011" species="ALL"/>
      </listOfProducts>
      <kineticLaw sboTerm="SBO:0000080">
        <notes>
          <body xmlns="http://www.w3.org/1999/xhtml">
            <p>kf_2 * BLL - kr_2 * ALL</p>
          </body>
        </notes>
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <apply>
            <times/>
            <ci> comp1 </ci>
            <apply>
              <minus/>
              <apply>
                <times/>
                <ci> kf_2 </ci>
                <ci> BLL </ci>
              </apply>
              <apply>
                <times/>
                <ci> kr_2 </ci>
                <ci> ALL </ci>
              </apply>
            </apply>
          </apply>
        </math>
      </kineticLaw>
    </reaction>
    <reaction metaid="_000019" id="React3" name="React3" sboTerm="SBO:0000177">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>first ligand on active</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000019">
            <bqbiol:is>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0042166"/>
              </rdf:Bag>
            </bqbiol:is>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
      <listOfReactants>
        <speciesReference sboTerm="SBO:0000010" species="A"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference sboTerm="SBO:0000011" species="AL"/>
      </listOfProducts>
      <kineticLaw sboTerm="SBO:0000080">
        <notes>
          <body xmlns="http://www.w3.org/1999/xhtml">
            <p>kf_3 * A - kr_3 * AL</p>
          </body>
        </notes>
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <apply>
            <times/>
            <ci> comp1 </ci>
            <apply>
              <minus/>
              <apply>
                <times/>
                <ci> kf_3 </ci>
                <ci> A </ci>
              </apply>
              <apply>
                <times/>
                <ci> kr_3 </ci>
                <ci> AL </ci>
              </apply>
            </apply>
          </apply>
        </math>
      </kineticLaw>
    </reaction>
    <reaction metaid="_000020" id="React4" name="React4" sboTerm="SBO:0000177">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>second ligand on active</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000020">
            <bqbiol:is>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0042166"/>
              </rdf:Bag>
            </bqbiol:is>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
      <listOfReactants>
        <speciesReference sboTerm="SBO:0000010" species="AL"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference sboTerm="SBO:0000011" species="ALL"/>
      </listOfProducts>
      <kineticLaw sboTerm="SBO:0000080">
        <notes>
          <body xmlns="http://www.w3.org/1999/xhtml">
            <p>kf_4 * AL - kr_4 * ALL</p>
          </body>
        </notes>
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <apply>
            <times/>
            <ci> comp1 </ci>
            <apply>
              <minus/>
              <apply>
                <times/>
                <ci> kf_4 </ci>
                <ci> AL </ci>
              </apply>
              <apply>
                <times/>
                <ci> kr_4 </ci>
                <ci> ALL </ci>
              </apply>
            </apply>
          </apply>
        </math>
      </kineticLaw>
    </reaction>
    <reaction metaid="_000021" id="React5" name="React5" sboTerm="SBO:0000181">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>opening of unliganded</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000021">
            <bqbiol:is>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0004889"/>
              </rdf:Bag>
            </bqbiol:is>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
      <listOfReactants>
        <speciesReference sboTerm="SBO:0000010" species="B"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference sboTerm="SBO:0000011" species="A"/>
      </listOfProducts>
      <kineticLaw sboTerm="SBO:0000080">
        <notes>
          <body xmlns="http://www.w3.org/1999/xhtml">
            <p>kf_5 * B - kr_5 * A</p>
          </body>
        </notes>
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <apply>
            <times/>
            <ci> comp1 </ci>
            <apply>
              <minus/>
              <apply>
                <times/>
                <ci> kf_5 </ci>
                <ci> B </ci>
              </apply>
              <apply>
                <times/>
                <ci> kr_5 </ci>
                <ci> A </ci>
              </apply>
            </apply>
          </apply>
        </math>
      </kineticLaw>
    </reaction>
    <reaction metaid="_000022" id="React6" name="React6" sboTerm="SBO:0000181">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>opening of monoliganded</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000022">
            <bqbiol:is>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0004889"/>
              </rdf:Bag>
            </bqbiol:is>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
      <listOfReactants>
        <speciesReference sboTerm="SBO:0000010" species="BL"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference sboTerm="SBO:0000011" species="AL"/>
      </listOfProducts>
      <kineticLaw sboTerm="SBO:0000080">
        <notes>
          <body xmlns="http://www.w3.org/1999/xhtml">
            <p>kf_6 * BL - kr_6 * AL</p>
          </body>
        </notes>
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <apply>
            <times/>
            <ci> comp1 </ci>
            <apply>
              <minus/>
              <apply>
                <times/>
                <ci> kf_6 </ci>
                <ci> BL </ci>
              </apply>
              <apply>
                <times/>
                <ci> kr_6 </ci>
                <ci> AL </ci>
              </apply>
            </apply>
          </apply>
        </math>
      </kineticLaw>
    </reaction>
    <reaction metaid="_000023" id="React7" name="React7" sboTerm="SBO:0000177">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>first ligand on intermediate</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000023">
            <bqbiol:is>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0042166"/>
              </rdf:Bag>
            </bqbiol:is>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
      <listOfReactants>
        <speciesReference sboTerm="SBO:0000010" species="I"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference sboTerm="SBO:0000011" species="IL"/>
      </listOfProducts>
      <kineticLaw sboTerm="SBO:0000080">
        <notes>
          <body xmlns="http://www.w3.org/1999/xhtml">
            <p>kf_7 * I - kr_7 * IL</p>
          </body>
        </notes>
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <apply>
            <times/>
            <ci> comp1 </ci>
            <apply>
              <minus/>
              <apply>
                <times/>
                <ci> kf_7 </ci>
                <ci> I </ci>
              </apply>
              <apply>
                <times/>
                <ci> kr_7 </ci>
                <ci> IL </ci>
              </apply>
            </apply>
          </apply>
        </math>
      </kineticLaw>
    </reaction>
    <reaction metaid="_000024" id="React8" name="React8" sboTerm="SBO:0000177">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>second ligand on intermediate</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000024">
            <bqbiol:is>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0042166"/>
              </rdf:Bag>
            </bqbiol:is>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
      <listOfReactants>
        <speciesReference sboTerm="SBO:0000010" species="IL"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference sboTerm="SBO:0000011" species="ILL"/>
      </listOfProducts>
      <kineticLaw sboTerm="SBO:0000080">
        <notes>
          <body xmlns="http://www.w3.org/1999/xhtml">
            <p>kf_8 * IL - kr_8 * ILL</p>
          </body>
        </notes>
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <apply>
            <times/>
            <ci> comp1 </ci>
            <apply>
              <minus/>
              <apply>
                <times/>
                <ci> kf_8 </ci>
                <ci> IL </ci>
              </apply>
              <apply>
                <times/>
                <ci> kr_8 </ci>
                <ci> ILL </ci>
              </apply>
            </apply>
          </apply>
        </math>
      </kineticLaw>
    </reaction>
    <reaction metaid="_000025" id="React9" name="React9" sboTerm="SBO:0000181">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>unliganded active &lt;=&gt; unliganded intermediate</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000025">
            <bqbiol:is>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0004889"/>
              </rdf:Bag>
            </bqbiol:is>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
      <listOfReactants>
        <speciesReference sboTerm="SBO:0000010" species="A"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference sboTerm="SBO:0000011" species="I"/>
      </listOfProducts>
      <kineticLaw sboTerm="SBO:0000080">
        <notes>
          <body xmlns="http://www.w3.org/1999/xhtml">
            <p>kf_9 * A - kr_9 * I</p>
          </body>
        </notes>
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <apply>
            <times/>
            <ci> comp1 </ci>
            <apply>
              <minus/>
              <apply>
                <times/>
                <ci> kf_9 </ci>
                <ci> A </ci>
              </apply>
              <apply>
                <times/>
                <ci> kr_9 </ci>
                <ci> I </ci>
              </apply>
            </apply>
          </apply>
        </math>
      </kineticLaw>
    </reaction>
    <reaction metaid="_000026" id="React10" name="React10" sboTerm="SBO:0000181">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>monoliganded active &lt;=&gt; monoliganded intermediate</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000026">
            <bqbiol:is>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0004889"/>
              </rdf:Bag>
            </bqbiol:is>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
      <listOfReactants>
        <speciesReference sboTerm="SBO:0000010" species="AL"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference sboTerm="SBO:0000011" species="IL"/>
      </listOfProducts>
      <kineticLaw sboTerm="SBO:0000080">
        <notes>
          <body xmlns="http://www.w3.org/1999/xhtml">
            <p>kf_10 * AL - kr_10 * IL</p>
          </body>
        </notes>
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <apply>
            <times/>
            <ci> comp1 </ci>
            <apply>
              <minus/>
              <apply>
                <times/>
                <ci> kf_10 </ci>
                <ci> AL </ci>
              </apply>
              <apply>
                <times/>
                <ci> kr_10 </ci>
                <ci> IL </ci>
              </apply>
            </apply>
          </apply>
        </math>
      </kineticLaw>
    </reaction>
    <reaction metaid="_000027" id="React11" name="React11" sboTerm="SBO:0000181">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>biliganded active &lt;=&gt; biliganded intermediate</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000027">
            <bqbiol:is>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0004889"/>
              </rdf:Bag>
            </bqbiol:is>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
      <listOfReactants>
        <speciesReference sboTerm="SBO:0000010" species="ALL"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference sboTerm="SBO:0000011" species="ILL"/>
      </listOfProducts>
      <kineticLaw sboTerm="SBO:0000080">
        <notes>
          <body xmlns="http://www.w3.org/1999/xhtml">
            <p>kf_11 * ALL - kr_11 * ILL</p>
          </body>
        </notes>
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <apply>
            <times/>
            <ci> comp1 </ci>
            <apply>
              <minus/>
              <apply>
                <times/>
                <ci> kf_11 </ci>
                <ci> ALL </ci>
              </apply>
              <apply>
                <times/>
                <ci> kr_11 </ci>
                <ci> ILL </ci>
              </apply>
            </apply>
          </apply>
        </math>
      </kineticLaw>
    </reaction>
    <reaction metaid="_000028" id="React12" name="React12" sboTerm="SBO:0000177">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>first ligand on desensitised</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000028">
            <bqbiol:is>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0042166"/>
              </rdf:Bag>
            </bqbiol:is>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
      <listOfReactants>
        <speciesReference sboTerm="SBO:0000010" species="D"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference sboTerm="SBO:0000011" species="DL"/>
      </listOfProducts>
      <kineticLaw sboTerm="SBO:0000080">
        <notes>
          <body xmlns="http://www.w3.org/1999/xhtml">
            <p>kf_12 * D - kr_12 * DL</p>
          </body>
        </notes>
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <apply>
            <times/>
            <ci> comp1 </ci>
            <apply>
              <minus/>
              <apply>
                <times/>
                <ci> kf_12 </ci>
                <ci> D </ci>
              </apply>
              <apply>
                <times/>
                <ci> kr_12 </ci>
                <ci> DL </ci>
              </apply>
            </apply>
          </apply>
        </math>
      </kineticLaw>
    </reaction>
    <reaction metaid="_000029" id="React13" name="React13" sboTerm="SBO:0000177">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>second ligand on desensitised</p>
        </body>
      </notes>
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_000029">
            <bqbiol:is>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0042166"/>
              </rdf:Bag>
            </bqbiol:is>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
      <listOfReactants>
        <speciesReference sboTerm="SBO:0000010" species="DL"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference sboTerm="SBO:0000011" species="DLL"/>
      </listOfProducts>
      <kineticLaw sboTerm="SBO:0000080">
        <notes>
          <body xmlns="http://www.w3.org/1999/xhtml">
            <p>kf_13 * DL - kr_13 * DLL</p>
          </body>
        </notes>
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <apply>
            <times/>
            <ci> comp1 </ci>
            <apply>
              <minus/>
              <apply>
                <times/>
                <ci> kf_13 </ci>
                <ci> DL </ci>
              </apply>
              <apply>
                <times/>
                <ci> kr_13 </ci>
                <ci> DLL </ci>
              </apply>
            </apply>
          </apply>
        </math>
      </kineticLaw>
    </reaction>
    <reaction metaid="_000030" id="React14" name="React14" sboTerm="SBO:0000181">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>unliganded intermediate &lt;=&gt; unliganded desensitised</p>
        </body>
      </notes>
      <listOfReactants>
        <speciesReference sboTerm="SBO:0000010" species="I"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference sboTerm="SBO:0000011" species="D"/>
      </listOfProducts>
      <kineticLaw sboTerm="SBO:0000080">
        <notes>
          <body xmlns="http://www.w3.org/1999/xhtml">
            <p>kf_14 * I - kr_14 * D</p>
          </body>
        </notes>
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <apply>
            <times/>
            <ci> comp1 </ci>
            <apply>
              <minus/>
              <apply>
                <times/>
                <ci> kf_14 </ci>
                <ci> I </ci>
              </apply>
              <apply>
                <times/>
                <ci> kr_14 </ci>
                <ci> D </ci>
              </apply>
            </apply>
          </apply>
        </math>
      </kineticLaw>
    </reaction>
    <reaction metaid="_000031" id="React15" name="React15" sboTerm="SBO:0000181">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>monoliganded intermediate &lt;=&gt; monoliganded desensitised</p>
        </body>
      </notes>
      <listOfReactants>
        <speciesReference sboTerm="SBO:0000010" species="IL"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference sboTerm="SBO:0000011" species="DL"/>
      </listOfProducts>
      <kineticLaw sboTerm="SBO:0000080">
        <notes>
          <body xmlns="http://www.w3.org/1999/xhtml">
            <p>kf_15 * IL - kr_15 * DL</p>
          </body>
        </notes>
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <apply>
            <times/>
            <ci> comp1 </ci>
            <apply>
              <minus/>
              <apply>
                <times/>
                <ci> kf_15 </ci>
                <ci> IL </ci>
              </apply>
              <apply>
                <times/>
                <ci> kr_15 </ci>
                <ci> DL </ci>
              </apply>
            </apply>
          </apply>
        </math>
      </kineticLaw>
    </reaction>
    <reaction metaid="_000032" id="React16" name="React16" sboTerm="SBO:0000181">
      <notes>
        <body xmlns="http://www.w3.org/1999/xhtml">
          <p>biliganded intermediate &lt;=&gt; biliganded desensitised</p>
        </body>
      </notes>
      <listOfReactants>
        <speciesReference sboTerm="SBO:0000010" species="ILL"/>
      </listOfReactants>
      <listOfProducts>
        <speciesReference sboTerm="SBO:0000011" species="DLL"/>
      </listOfProducts>
      <kineticLaw sboTerm="SBO:0000080">
        <notes>
          <body xmlns="http://www.w3.org/1999/xhtml">
            <p>kf_16 * ILL - kr_16 * DLL</p>
          </body>
        </notes>
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <apply>
            <times/>
            <ci> comp1 </ci>
            <apply>
              <minus/>
              <apply>
                <times/>
                <ci> kf_16 </ci>
                <ci> ILL </ci>
              </apply>
              <apply>
                <times/>
                <ci> kr_16 </ci>
                <ci> DLL </ci>
              </apply>
            </apply>
          </apply>
        </math>
      </kineticLaw>
    </reaction>
  </listOfReactions>
  <listOfEvents>
    <event metaid="_180306" id="RemovalACh" name="removal of ACh">
      <annotation>
        <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
          <rdf:Description rdf:about="#_180306">
            <bqbiol:is>
              <rdf:Bag>
                <rdf:li rdf:resource="urn:miriam:obo.go:GO%3A0001507"/>
              </rdf:Bag>
            </bqbiol:is>
          </rdf:Description>
        </rdf:RDF>
      </annotation>
      <trigger>
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <apply>
            <gt/>
            <csymbol encoding="text" definitionURL="http://www.sbml.org/sbml/symbols/time"> time </csymbol>
            <ci> t2 </ci>
          </apply>
        </math>
      </trigger>
      <listOfEventAssignments>
        <eventAssignment variable="kf_0">
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <cn> 0 </cn>
          </math>
        </eventAssignment>
        <eventAssignment variable="kf_3">
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <cn> 0 </cn>
          </math>
        </eventAssignment>
        <eventAssignment variable="kf_7">
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <cn> 0 </cn>
          </math>
        </eventAssignment>
        <eventAssignment variable="kf_12">
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <cn> 0 </cn>
          </math>
        </eventAssignment>
        <eventAssignment variable="kf_1">
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <cn> 0 </cn>
          </math>
        </eventAssignment>
        <eventAssignment variable="kf_4">
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <cn> 0 </cn>
          </math>
        </eventAssignment>
        <eventAssignment variable="kf_8">
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <cn> 0 </cn>
          </math>
        </eventAssignment>
        <eventAssignment variable="kf_13">
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <cn> 0 </cn>
          </math>
        </eventAssignment>
      </listOfEventAssignments>
    </event>
  </listOfEvents>
</model>
</sbml>"

def upload():
	session.SBML = request.vars.SBML
	session.bioGraph = biographer.Graph( SBMLinput=session.SBML )
	del session.bioGraph.SBML
	return redirect(URL(r=request,c='Workbench',f='index'))

