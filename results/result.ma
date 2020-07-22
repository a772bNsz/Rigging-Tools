//Maya ASCII 2019 scene
//Name: result.ma
//Last modified: Fri, Jul 24, 2020 01:18:16 AM
//Codeset: ANSI_X3.4-1968
requires maya "2019";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2019";
fileInfo "version" "2019";
fileInfo "cutIdentifier" "201812112215-434d8d9c04";
fileInfo "osv" "Linux 4.19.76-linuxkit #1 SMP Tue May 26 11:42:35 UTC 2020 x86_64";
createNode transform -s -n "persp";
	rename -uid "36CB8740-0000-0006-5F1A-36D800000211";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 28 21 28 ;
	setAttr ".r" -type "double3" -27.938352729602379 44.999999999999972 -5.172681101354183e-14 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "36CB8740-0000-0006-5F1A-36D800000212";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 44.82186966202994;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "36CB8740-0000-0006-5F1A-36D800000213";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "36CB8740-0000-0006-5F1A-36D800000214";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "36CB8740-0000-0006-5F1A-36D800000215";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "36CB8740-0000-0006-5F1A-36D800000216";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "36CB8740-0000-0006-5F1A-36D800000217";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "36CB8740-0000-0006-5F1A-36D800000218";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "src";
	rename -uid "36CB8740-0000-0006-5F1A-36D800000222";
createNode mesh -n "srcShape" -p "src";
	rename -uid "36CB8740-0000-0006-5F1A-36D800000221";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 10 ".uvst[0].uvsp[0:9]" -type "float2" 0.50187975 0 0.0018796921
		 0.24999999 0.50187969 0.5 1.0018796921 0.25 0 0.5 0.25 0.5 0.5 0.5 0.75 0.5 1 0.5
		 0.5 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 5 ".vt[0:4]"  1.3113416e-07 -1 -1 -1 -1 -8.7422777e-08
		 -4.3711388e-08 -1 1 1 -1 0 0 1 0;
	setAttr -s 8 ".ed[0:7]"  0 1 0 1 2 0 2 3 0 3 0 0 0 4 0 1 4 0 2 4 0
		 3 4 0;
	setAttr -s 5 -ch 16 ".fc[0:4]" -type "polyFaces" 
		f 4 -4 -3 -2 -1
		mu 0 4 0 3 2 1
		f 3 0 5 -5
		mu 0 3 4 5 9
		f 3 1 6 -6
		mu 0 3 5 6 9
		f 3 2 7 -7
		mu 0 3 6 7 9
		f 3 3 4 -8
		mu 0 3 7 8 9;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
createNode transform -n "trg";
	rename -uid "36CB8740-0000-0006-5F1A-36D800000225";
	setAttr ".t" -type "double3" 26.873815688888889 -1.7507712666666677 1.1499473703703709 ;
	setAttr ".r" -type "double3" 0.84558711111111096 0.75205822222222218 17.095677333333335 ;
createNode mesh -n "trgShape" -p "trg";
	rename -uid "36CB8740-0000-0006-5F1A-36D800000224";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 26 ".uvst[0].uvsp[0:25]" -type "float2" 0.93489242 0.125
		 0.75187969 0.033493653 0.50187969 0 0.25187969 0.033493653 0.068866998 0.125 0.0018796921
		 0.25 0.068866998 0.375 0.25187969 0.46650636 0.50187969 0.5 0.75187969 0.46650636
		 0.93489242 0.375 1.0018796921 0.25 0 0.5 0.083333336 0.5 0.16666667 0.5 0.25 0.5
		 0.33333334 0.5 0.41666669 0.5 0.5 0.5 0.58333331 0.5 0.66666663 0.5 0.74999994 0.5
		 0.83333325 0.5 0.91666657 0.5 0.99999988 0.5 0.5 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 13 ".vt[0:12]"  0.43301269 -2.5 -0.25 0.25 -2.5 -0.43301269
		 0 -2.5 -0.5 -0.25 -2.5 -0.43301269 -0.43301269 -2.5 -0.25 -0.5 -2.5 0 -0.43301269 -2.5 0.25
		 -0.25 -2.5 0.43301269 0 -2.5 0.5 0.25 -2.5 0.43301269 0.43301269 -2.5 0.25 0.5 -2.5 0
		 0 2.5 0;
	setAttr -s 24 ".ed[0:23]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 0 0 0 12 0 1 12 0 2 12 0 3 12 0 4 12 0 5 12 0 6 12 0
		 7 12 0 8 12 0 9 12 0 10 12 0 11 12 0;
	setAttr -s 13 -ch 48 ".fc[0:12]" -type "polyFaces" 
		f 12 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
		mu 0 12 0 11 10 9 8 7 6 5 4 3 2 1
		f 3 0 13 -13
		mu 0 3 12 13 25
		f 3 1 14 -14
		mu 0 3 13 14 25
		f 3 2 15 -15
		mu 0 3 14 15 25
		f 3 3 16 -16
		mu 0 3 15 16 25
		f 3 4 17 -17
		mu 0 3 16 17 25
		f 3 5 18 -18
		mu 0 3 17 18 25
		f 3 6 19 -19
		mu 0 3 18 19 25
		f 3 7 20 -20
		mu 0 3 19 20 25
		f 3 8 21 -21
		mu 0 3 20 21 25
		f 3 9 22 -22
		mu 0 3 21 22 25
		f 3 10 23 -23
		mu 0 3 22 23 25
		f 3 11 12 -24
		mu 0 3 23 24 25;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ndt" 0;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "36CB8740-0000-0006-5F1A-36D800000219";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "36CB8740-0000-0006-5F1A-36D80000021A";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "36CB8740-0000-0006-5F1A-36D80000021B";
createNode displayLayerManager -n "layerManager";
	rename -uid "36CB8740-0000-0006-5F1A-36D80000021C";
createNode displayLayer -n "defaultLayer";
	rename -uid "36CB8740-0000-0006-5F1A-36D80000021D";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "36CB8740-0000-0006-5F1A-36D80000021E";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "36CB8740-0000-0006-5F1A-36D80000021F";
	setAttr ".g" yes;
createNode animCurveTA -n "src_rotateX";
	rename -uid "36CB8740-0000-0006-5F1A-36D80000023E";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  13 0 19 11.415426 27 0;
createNode animCurveTA -n "src_rotateY";
	rename -uid "36CB8740-0000-0006-5F1A-36D80000023F";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  13 0 19 10.152786 27 0;
createNode animCurveTA -n "src_rotateZ";
	rename -uid "36CB8740-0000-0006-5F1A-36D800000240";
	setAttr ".tan" 3;
	setAttr -s 5 ".ktv[0:4]"  13 0 16 51.287032 19 -131.12118 22 -73.831704
		 27 -2.4406911;
	setAttr -s 5 ".kit[1:4]"  2 3 1 3;
	setAttr -s 5 ".kot[0:4]"  2 3 3 1 3;
	setAttr -s 5 ".ktl[3:4]" no yes;
	setAttr -s 5 ".kix[3:4]"  0.0012115101056272384 0.20833333333333337;
	setAttr -s 5 ".kiy[3:4]"  3.6707791958603448 0;
	setAttr -s 5 ".kox[3:4]"  0 0.20833333333333337;
	setAttr -s 5 ".koy[3:4]"  19.769356137537621 0;
createNode animCurveTL -n "src_translateX";
	rename -uid "36CB8740-0000-0006-5F1A-36D800000241";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  13 32.545374 16 9.1922987999999997 19 7.4690567999999997 22 16.147648
		 27 32.545374;
createNode animCurveTL -n "src_translateY";
	rename -uid "36CB8740-0000-0006-5F1A-36D800000242";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  13 -3.7114009000000001 16 7.3459180999999996 19 20.752832 22 5.7356467999999996
		 27 -3.7114009000000001;
createNode animCurveTL -n "src_translateZ";
	rename -uid "36CB8740-0000-0006-5F1A-36D800000243";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 5 ".ktv[0:4]"  13 -5.2621133999999996 16 19.470121 19 -10.562566 22 2.4632863999999999
		 27 -5.2621133999999996;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "36CB8740-0000-0006-5F1A-36D800000274";
	setAttr ".b" -type "string" "// Maya Mel UI Configuration File.\n// No UI generated in batch mode.\n";
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "36CB8740-0000-0006-5F1A-36D800000275";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr -s 2 ".dsm";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
connectAttr "src_rotateX.o" "src.rx";
connectAttr "src_rotateY.o" "src.ry";
connectAttr "src_rotateZ.o" "src.rz";
connectAttr "src_translateX.o" "src.tx";
connectAttr "src_translateY.o" "src.ty";
connectAttr "src_translateZ.o" "src.tz";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "srcShape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "trgShape.iog" ":initialShadingGroup.dsm" -na;
// End of result.ma
