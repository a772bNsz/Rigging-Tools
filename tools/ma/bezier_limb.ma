//Maya ASCII 2019 scene
//Name: result.ma
//Last modified: Mon, Aug 24, 2020 06:43:45 AM
//Codeset: ANSI_X3.4-1968
requires maya "2019";
requires -nodeType "decomposeMatrix" "matrixNodes" "1.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2019";
fileInfo "version" "2019";
fileInfo "cutIdentifier" "201812112215-434d8d9c04";
fileInfo "osv" "Linux 4.19.76-linuxkit #1 SMP Tue May 26 11:42:35 UTC 2020 x86_64";
createNode transform -s -n "persp";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000037F";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 28 21 28 ;
	setAttr ".r" -type "double3" -27.938352729602379 44.999999999999972 -5.172681101354183e-14 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000380";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 44.82186966202994;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000381";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -89.999999999999986 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000382";
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
	rename -uid "7A4DA740-0000-0007-5F43-61A100000383";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000384";
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
	rename -uid "7A4DA740-0000-0007-5F43-61A100000385";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 89.999999999999986 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000386";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "group1";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000038E";
createNode joint -n "joint1" -p "group1";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000038F";
	setAttr ".t" -type "double3" -5 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 11.309932474020197 0 ;
	setAttr ".radi" 0.71201825070307501;
createNode joint -n "joint2" -p "joint1";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000390";
	setAttr ".t" -type "double3" 5.0990195135927854 0 -1.4432899320127035e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -22.619864948040405 0 ;
	setAttr ".radi" 0.71201825070307501;
createNode joint -n "joint3" -p "joint2";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000391";
	setAttr ".t" -type "double3" 5.0990195135927845 0 1.1102230246251565e-15 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 11.309932474020204 0 ;
	setAttr ".radi" 0.71201825070307501;
createNode ikEffector -n "effector1" -p "joint2";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000392";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode transform -n "locator1" -p "group1";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000393";
	setAttr ".t" -type "double3" 5 0 0 ;
createNode locator -n "locatorShape1" -p "locator1";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000394";
	setAttr -k off ".v";
createNode ikHandle -n "ikHandle1" -p "locator1";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000395";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 8.8817841970012523e-16 0 2.2204460492503131e-16 ;
	setAttr ".r" -type "double3" 0 -11.309932474020204 0 ;
	setAttr ".roc" yes;
createNode transform -n "bezier_aim_GRP" -p "group1";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000396";
createNode transform -n "start_GRP" -p "bezier_aim_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000397";
	setAttr ".s" -type "double3" 1 1 0.99999999999999989 ;
createNode transform -n "start_read_NUL" -p "start_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000398";
createNode transform -n "cluster6Handle" -p "start_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000399";
	setAttr ".t" -type "double3" -5 0 0 ;
	setAttr ".rp" -type "double3" 5 0 0 ;
	setAttr ".sp" -type "double3" 5 0 0 ;
createNode clusterHandle -n "cluster6HandleShape" -p "cluster6Handle";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000039A";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" 5 0 0 ;
createNode parentConstraint -n "start_GRP_parentConstraint1" -p "start_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000039B";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "joint1W0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tor" -type "double3" 0 3.1805546814635176e-15 0 ;
	setAttr ".lr" -type "double3" 0 11.309932474020199 0 ;
	setAttr ".rst" -type "double3" -5 0 0 ;
	setAttr ".rsrr" -type "double3" 0 11.309932474020199 0 ;
	setAttr -k on ".w0";
createNode transform -n "end_GRP" -p "bezier_aim_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000039C";
createNode transform -n "end_read_NUL" -p "end_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000039D";
	setAttr ".r" -type "double3" 0 11.309932474020203 0 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1 ;
createNode transform -n "cluster5Handle" -p "end_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000039E";
	setAttr ".t" -type "double3" 5.0000000000000018 0 -1.1657341758564144e-15 ;
	setAttr ".rp" -type "double3" -5 0 0 ;
	setAttr ".sp" -type "double3" -5 0 0 ;
createNode clusterHandle -n "cluster5HandleShape" -p "cluster5Handle";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000039F";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".or" -type "double3" -5 0 0 ;
createNode parentConstraint -n "end_GRP_parentConstraint1" -p "end_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003A0";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "locator1W0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 5 0 0 ;
	setAttr -k on ".w0";
createNode transform -n "curve1" -p "bezier_aim_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003A1";
	setAttr ".it" no;
createNode nurbsCurve -n "curveShape1" -p "curve1";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003A2";
	setAttr -k off ".v";
	setAttr -s 6 ".iog[0].og";
	setAttr ".tw" yes;
createNode nurbsCurve -n "curveShape1Orig" -p "curve1";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003A3";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		-5 0 0
		5 0 0
		;
createNode joint -n "bezier_aim_RVT" -p "bezier_aim_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003A4";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".it" no;
	setAttr ".dla" yes;
	setAttr ".ssc" no;
createNode aimConstraint -n "bezier_aim_RVT_aimConstraint1" -p "bezier_aim_RVT";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003A5";
createNode transform -n "upv_LOC" -p "bezier_aim_RVT";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003A6";
	setAttr ".t" -type "double3" 8.8817841970012513e-16 3 -1.4571696306096124e-16 ;
createNode locator -n "upv_LOCShape" -p "upv_LOC";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003A7";
	setAttr -k off ".v";
createNode transform -n "aim_LOC" -p "bezier_aim_RVT";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003A8";
	setAttr ".t" -type "double3" 8.8817841970012523e-16 0 -3 ;
createNode locator -n "aim_LOCShape" -p "aim_LOC";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003A9";
	setAttr -k off ".v";
createNode transform -n "cartoony_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003D2";
createNode transform -n "lower_GRP" -p "cartoony_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003D3";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1 0 0 ;
createNode transform -n "rivet1_OFS" -p "lower_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003D4";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
createNode joint -n "seg1_JNT" -p "|cartoony_GRP|lower_GRP|rivet1_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003D5";
	addAttr -ci true -sn "position" -ln "position" -at "float";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.1232338493354837e-18 -2.2204460492503131e-16 -2.4651903288156619e-32 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 -7.0622500768802529e-31 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 1.0000000000000002 -4.9303806576313238e-32 1.2246467991473535e-16 0 -2.2204460492503128e-16 1.0000000000000002 1.224646799147353e-16 0
		 -1.2246467991473532e-16 -1.2246467991473532e-16 1 0 -2.0976023332915122e-16 6.1232338493355338e-18 -2.5407181807812022e-33 1;
	setAttr ".radi" 0.05;
createNode transform -n "rivet2_OFS" -p "lower_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003D6";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
createNode joint -n "seg2_JNT" -p "|cartoony_GRP|lower_GRP|rivet2_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003D7";
	addAttr -ci true -sn "position" -ln "position" -at "float";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.1232334816994559e-18 -1.65568569965302e-09 5.5511151028494813e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 -7.0622500768802529e-31 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 1.0000000000000002 -4.9303806576313238e-32 1.2246467991473535e-16 0 -2.2204460492503128e-16 1.0000000000000002 1.224646799147353e-16 0
		 -1.2246467991473532e-16 -1.2246467991473532e-16 1 0 0.22222222235281169 6.1232338493355338e-18 -5.5511151231257827e-17 1;
	setAttr ".radi" 0.05;
	setAttr ".position" 0.1111111119389534;
createNode transform -n "rivet3_OFS" -p "lower_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003D8";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
createNode joint -n "seg3_JNT" -p "|cartoony_GRP|lower_GRP|rivet3_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003D9";
	addAttr -ci true -sn "position" -ln "position" -at "float";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.123233114063798e-18 -3.3113695119268982e-09 1.3877787402288651e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 -7.0622500768802529e-31 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 1.0000000000000002 -4.9303806576313238e-32 1.2246467991473535e-16 0 -2.2204460492503128e-16 1.0000000000000002 1.224646799147353e-16 0
		 -1.2246467991473532e-16 -1.2246467991473532e-16 1 0 0.44444444447118192 6.1232338493355338e-18 -1.3877787807814457e-17 1;
	setAttr ".radi" 0.05;
	setAttr ".position" 0.2222222238779068;
createNode transform -n "rivet4_OFS" -p "lower_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003DA";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
createNode joint -n "seg4_JNT" -p "|cartoony_GRP|lower_GRP|rivet4_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003DB";
	addAttr -ci true -sn "position" -ln "position" -at "float";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.1232294377054802e-18 -1.9868215461738004e-08 1.3877788051129921e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 7.0622500768802529e-31 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 1.0000000000000002 -7.3955709864469857e-32 -1.2246467991473535e-16 0 -2.2204460492503131e-16 1 -1.224646799147353e-16 0
		 1.2246467991473532e-16 1.224646799147353e-16 1 0 0.66666666666900931 6.1232338493355322e-18 -1.3877787807814457e-16 1;
	setAttr ".radi" 0.05;
	setAttr ".position" 0.3333333432674408;
createNode transform -n "rivet5_OFS" -p "lower_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003DC";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
createNode joint -n "seg5_JNT" -p "|cartoony_GRP|lower_GRP|rivet5_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003DD";
	addAttr -ci true -sn "position" -ln "position" -at "float";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.1232323787920475e-18 -6.6227391071205233e-09 1.387778788891962e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 7.0622500768802529e-31 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 1.0000000000000002 -7.3955709864469857e-32 -1.2246467991473535e-16 0 -2.2204460492503131e-16 1 -1.224646799147353e-16 0
		 1.2246467991473532e-16 1.224646799147353e-16 1 0 0.88888888888848561 6.1232338493355353e-18 -1.3877787807814457e-16 1;
	setAttr ".radi" 0.05;
	setAttr ".position" 0.4444444477558136;
createNode transform -n "rivet6_OFS" -p "lower_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003DE";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
createNode joint -n "seg6_JNT" -p "|cartoony_GRP|lower_GRP|rivet6_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003DF";
	addAttr -ci true -sn "position" -ln "position" -at "float";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.1232220849888078e-18 -5.2981907527893668e-08 5.5511144742845475e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 -7.0622500768802529e-31 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 1.0000000000000002 -4.9303806576313238e-32 1.2246467991473535e-16 0 -2.2204460492503128e-16 1.0000000000000002 1.224646799147353e-16 0
		 -1.2246467991473532e-16 -1.2246467991473532e-16 1 0 1.1111111111115128 6.1232338493355338e-18 -5.5511151231257821e-17 1;
	setAttr ".radi" 0.05;
	setAttr ".position" 0.55555558204650879;
createNode transform -n "rivet7_OFS" -p "lower_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003E0";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
createNode joint -n "seg7_JNT" -p "|cartoony_GRP|lower_GRP|rivet7_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003E1";
	addAttr -ci true -sn "position" -ln "position" -at "float";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.1232250260753658e-18 -3.9736431201031763e-08 -1.3877792674123782e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 -7.0622500768802529e-31 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 1.0000000000000002 -7.3955709864469857e-32 1.2246467991473535e-16 0 -2.2204460492503131e-16 1 1.224646799147353e-16 0
		 -1.2246467991473532e-16 -1.224646799147353e-16 1 0 1.3333333333309891 6.1232338493355322e-18 1.3877787807814454e-17 1;
	setAttr ".radi" 0.05;
	setAttr ".position" 0.66666668653488159;
createNode transform -n "rivet8_OFS" -p "lower_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003E2";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
createNode joint -n "seg8_JNT" -p "|cartoony_GRP|lower_GRP|rivet8_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003E3";
	addAttr -ci true -sn "position" -ln "position" -at "float";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.1232279671620964e-18 -2.6490954097013741e-08 8.3266730091092953e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 7.0622500768802529e-31 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 1.0000000000000002 -4.9303806576313238e-32 -1.2246467991473535e-16 0 -2.2204460492503128e-16 1.0000000000000002 -1.224646799147353e-16 0
		 1.2246467991473532e-16 1.2246467991473532e-16 1 0 1.5555555555288179 6.1232338493355338e-18 -8.3266726846886741e-17 1;
	setAttr ".radi" 0.05;
	setAttr ".position" 0.77777779102325439;
createNode transform -n "rivet9_OFS" -p "lower_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003E4";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
createNode joint -n "seg9_JNT" -p "|cartoony_GRP|lower_GRP|rivet9_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003E5";
	addAttr -ci true -sn "position" -ln "position" -at "float";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.1232309082486915e-18 -1.3245477714640685e-08 9.7144516276804384e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 7.0622500768802529e-31 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 1.0000000000000002 -4.9303806576313238e-32 -1.2246467991473535e-16 0 -2.2204460492503128e-16 1.0000000000000002 -1.224646799147353e-16 0
		 1.2246467991473532e-16 1.2246467991473532e-16 1 0 1.7777777776471866 6.1232338493355576e-18 -9.7144514654701197e-17 1;
	setAttr ".radi" 0.05;
	setAttr ".position" 0.8888888955116272;
createNode transform -n "rivet10_OFS" -p "lower_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003E6";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
createNode joint -n "seg10_JNT" -p "|cartoony_GRP|lower_GRP|rivet10_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003E7";
	addAttr -ci true -sn "position" -ln "position" -at "float";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.1232338493355338e-18 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 7.0622500768802529e-31 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 1.0000000000000002 -4.9303806576313238e-32 -1.2246467991473535e-16 0 -2.2204460492503128e-16 1.0000000000000002 -1.224646799147353e-16 0
		 1.2246467991473532e-16 1.2246467991473532e-16 1 0 2 6.1232338493355338e-18 0 1;
	setAttr ".radi" 0.05;
	setAttr ".position" 1;
createNode transform -n "nurbsPlane2" -p "lower_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003E8";
	setAttr ".v" no;
createNode nurbsSurface -n "nurbsPlaneShape2" -p "nurbsPlane2";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003E9";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr -av ".iog[0].og[1].gco";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".tw" yes;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dvu" 0;
	setAttr ".dvv" 0;
	setAttr ".cpr" 4;
	setAttr ".cps" 4;
	setAttr ".nufa" 4.5;
	setAttr ".nvfa" 4.5;
createNode nurbsSurface -n "nurbsPlaneShape1Orig2" -p "nurbsPlane2";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003EA";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".tw" yes;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dvu" 0;
	setAttr ".dvv" 0;
	setAttr ".cpr" 4;
	setAttr ".cps" 4;
createNode transform -n "ffd1Lattice1" -p "lower_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003EB";
	setAttr ".v" no;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr ".s" -type "double3" 2 9.9999999999999998e-13 0.2 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".it" no;
createNode lattice -n "ffd1Lattice1Shape" -p "ffd1Lattice1";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003EC";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".tw" yes;
	setAttr ".sd" 3;
	setAttr ".td" 2;
createNode lattice -n "ffd1Lattice1ShapeOrig" -p "ffd1Lattice1";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003ED";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".sd" 3;
	setAttr ".td" 2;
	setAttr ".cc" -type "lattice" 3 2 2 12 -0.5 -0.5 -0.5 0
		 -0.5 -0.5 0.5 -0.5 -0.5 -0.5 0.5 -0.5 0 0.5 -0.5 0.5
		 0.5 -0.5 -0.5 -0.5 0.5 0 -0.5 0.5 0.5 -0.5 0.5 -0.5
		 0.5 0.5 0 0.5 0.5 0.5 0.5 0.5 ;
createNode transform -n "ffd1Base1" -p "lower_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003EE";
	setAttr ".v" no;
	setAttr ".s" -type "double3" 2 9.9999999999999998e-13 0.2 ;
createNode baseLattice -n "ffd1Base1Shape" -p "ffd1Base1";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003EF";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
createNode transform -n "duplicatedCurve5" -p "lower_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003F0";
	setAttr ".v" no;
	setAttr ".it" no;
createNode nurbsCurve -n "duplicatedCurveShape5" -p "duplicatedCurve5";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003F1";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "duplicatedCurve4" -p "lower_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003F2";
	setAttr ".v" no;
	setAttr ".it" no;
createNode nurbsCurve -n "duplicatedCurveShape4" -p "duplicatedCurve4";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003F3";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "loftedSurface2" -p "lower_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003F4";
	setAttr ".it" no;
createNode nurbsSurface -n "loftedSurfaceShape2" -p "loftedSurface2";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003F5";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".tw" yes;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dvu" 0;
	setAttr ".dvv" 0;
	setAttr ".cpr" 4;
	setAttr ".cps" 4;
createNode transform -n "upper_GRP" -p "cartoony_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003F6";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -1 0 0 ;
createNode transform -n "rivet1_OFS" -p "upper_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003F7";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
createNode joint -n "seg1_JNT" -p "|cartoony_GRP|upper_GRP|rivet1_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003F8";
	addAttr -ci true -sn "position" -ln "position" -at "float";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".t" -type "double3" 6.1232338493354837e-18 -2.2204460492503131e-16 -2.4651903288156619e-32 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 -7.016709298534876e-15 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 1.0000000000000002 -7.3955709864469857e-32 1.2246467991473535e-16 0 -2.2204460492503131e-16 1 1.224646799147353e-16 0
		 -1.2246467991473532e-16 -1.224646799147353e-16 1 0 -2 6.1232338493355322e-18 -2.5407181807812022e-33 1;
	setAttr ".radi" 0.05;
createNode transform -n "rivet2_OFS" -p "upper_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003F9";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
createNode joint -n "seg2_JNT" -p "|cartoony_GRP|upper_GRP|rivet2_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003FA";
	addAttr -ci true -sn "position" -ln "position" -at "float";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.1232334816994559e-18 -1.65568569965302e-09 5.5511151028494813e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 -7.016709298534876e-15 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 1.0000000000000002 -7.3955709864469857e-32 1.2246467991473535e-16 0 -2.2204460492503131e-16 1 1.224646799147353e-16 0
		 -1.2246467991473532e-16 -1.224646799147353e-16 1 0 -1.7777777776471893 6.1232338493355322e-18 -5.5511151231257827e-17 1;
	setAttr ".radi" 0.05;
	setAttr ".position" 0.1111111119389534;
createNode transform -n "rivet3_OFS" -p "upper_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003FB";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
createNode joint -n "seg3_JNT" -p "|cartoony_GRP|upper_GRP|rivet3_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003FC";
	addAttr -ci true -sn "position" -ln "position" -at "float";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.123233114063798e-18 -3.3113695119268982e-09 1.3877787402288651e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 -7.016709298534876e-15 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 1.0000000000000002 -4.9303806576313238e-32 1.2246467991473535e-16 0 -2.2204460492503128e-16 1.0000000000000002 1.224646799147353e-16 0
		 -1.2246467991473532e-16 -1.2246467991473532e-16 1 0 -1.555555555528819 6.1232338493355338e-18 -1.3877787807814457e-17 1;
	setAttr ".radi" 0.05;
	setAttr ".position" 0.2222222238779068;
createNode transform -n "rivet4_OFS" -p "upper_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003FD";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
createNode joint -n "seg4_JNT" -p "|cartoony_GRP|upper_GRP|rivet4_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003FE";
	addAttr -ci true -sn "position" -ln "position" -at "float";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.1232294377054802e-18 -1.9868215461738004e-08 1.3877788051129921e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 7.016709298534876e-15 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 1.0000000000000002 -4.9303806576313238e-32 -1.2246467991473535e-16 0 -2.2204460492503128e-16 1.0000000000000002 -1.224646799147353e-16 0
		 1.2246467991473532e-16 1.2246467991473532e-16 1 0 -1.3333333333309914 6.1232338493355338e-18 -1.3877787807814457e-16 1;
	setAttr ".radi" 0.05;
	setAttr ".position" 0.3333333432674408;
createNode transform -n "rivet5_OFS" -p "upper_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003FF";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
createNode joint -n "seg5_JNT" -p "|cartoony_GRP|upper_GRP|rivet5_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000400";
	addAttr -ci true -sn "position" -ln "position" -at "float";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.1232323787920475e-18 -6.6227391071205233e-09 1.387778788891962e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 7.016709298534876e-15 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 1.0000000000000002 -4.9303806576313238e-32 -1.2246467991473535e-16 0 -2.2204460492503128e-16 1.0000000000000002 -1.224646799147353e-16 0
		 1.2246467991473532e-16 1.2246467991473532e-16 1 0 -1.1111111111115151 6.1232338493355361e-18 -1.3877787807814457e-16 1;
	setAttr ".radi" 0.05;
	setAttr ".position" 0.4444444477558136;
createNode transform -n "rivet6_OFS" -p "upper_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000401";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
createNode joint -n "seg6_JNT" -p "|cartoony_GRP|upper_GRP|rivet6_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000402";
	addAttr -ci true -sn "position" -ln "position" -at "float";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.1232220849888078e-18 -5.2981907527893668e-08 5.5511144742845475e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 -7.016709298534876e-15 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 1.0000000000000002 -4.9303806576313238e-32 1.2246467991473535e-16 0 -2.2204460492503128e-16 1.0000000000000002 1.224646799147353e-16 0
		 -1.2246467991473532e-16 -1.2246467991473532e-16 1 0 -0.88888888888848872 6.1232338493355338e-18 -5.5511151231257821e-17 1;
	setAttr ".radi" 0.05;
	setAttr ".position" 0.55555558204650879;
createNode transform -n "rivet7_OFS" -p "upper_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000403";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
createNode joint -n "seg7_JNT" -p "|cartoony_GRP|upper_GRP|rivet7_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000404";
	addAttr -ci true -sn "position" -ln "position" -at "float";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.1232250260753658e-18 -3.9736431201031763e-08 -1.3877792674123782e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 -7.016709298534876e-15 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 1.0000000000000002 -4.9303806576313238e-32 1.2246467991473535e-16 0 -2.2204460492503128e-16 1.0000000000000002 1.224646799147353e-16 0
		 -1.2246467991473532e-16 -1.2246467991473532e-16 1 0 -0.66666666666901131 6.1232338493355338e-18 1.3877787807814454e-17 1;
	setAttr ".radi" 0.05;
	setAttr ".position" 0.66666668653488159;
createNode transform -n "rivet8_OFS" -p "upper_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000405";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
createNode joint -n "seg8_JNT" -p "|cartoony_GRP|upper_GRP|rivet8_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000406";
	addAttr -ci true -sn "position" -ln "position" -at "float";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.1232279671620964e-18 -2.6490954097013741e-08 8.3266730091092953e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 7.016709298534876e-15 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 1.0000000000000002 -4.9303806576313238e-32 -1.2246467991473535e-16 0 -2.2204460492503128e-16 1.0000000000000002 -1.224646799147353e-16 0
		 1.2246467991473532e-16 1.2246467991473532e-16 1 0 -0.44444444447118309 6.1232338493355338e-18 -8.3266726846886741e-17 1;
	setAttr ".radi" 0.05;
	setAttr ".position" 0.77777779102325439;
createNode transform -n "rivet9_OFS" -p "upper_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000407";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
createNode joint -n "seg9_JNT" -p "|cartoony_GRP|upper_GRP|rivet9_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000408";
	addAttr -ci true -sn "position" -ln "position" -at "float";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.1232309082486915e-18 -1.3245477714640685e-08 9.7144516276804384e-17 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 7.016709298534876e-15 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 1.0000000000000002 -7.3955709864469857e-32 -1.2246467991473535e-16 0 -2.2204460492503131e-16 1 -1.224646799147353e-16 0
		 1.2246467991473532e-16 1.224646799147353e-16 1 0 -0.22222222235281364 6.1232338493355569e-18 -9.7144514654701197e-17 1;
	setAttr ".radi" 0.05;
	setAttr ".position" 0.8888888955116272;
createNode transform -n "rivet10_OFS" -p "upper_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000409";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
createNode joint -n "seg10_JNT" -p "|cartoony_GRP|upper_GRP|rivet10_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000040A";
	addAttr -ci true -sn "position" -ln "position" -at "float";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".t" -type "double3" 6.1232338493355338e-18 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 180 7.016709298534876e-15 89.999999999999986 ;
	setAttr ".bps" -type "matrix" 1.0000000000000002 -4.9303806576313238e-32 -1.2246467991473535e-16 0 -2.2204460492503128e-16 1.0000000000000002 -1.224646799147353e-16 0
		 1.2246467991473532e-16 1.2246467991473532e-16 1 0 -1.6543612237464242e-24 6.1232338493355338e-18 0 1;
	setAttr ".radi" 0.05;
	setAttr ".position" 1;
createNode transform -n "nurbsPlane1" -p "upper_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000040B";
	setAttr ".v" no;
createNode nurbsSurface -n "nurbsPlaneShape1" -p "nurbsPlane1";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000040C";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr -av ".iog[0].og[1].gco";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".tw" yes;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dvu" 0;
	setAttr ".dvv" 0;
	setAttr ".cpr" 4;
	setAttr ".cps" 4;
	setAttr ".nufa" 4.5;
	setAttr ".nvfa" 4.5;
createNode nurbsSurface -n "nurbsPlaneShape1Orig" -p "nurbsPlane1";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000040D";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".tw" yes;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dvu" 0;
	setAttr ".dvv" 0;
	setAttr ".cpr" 4;
	setAttr ".cps" 4;
createNode transform -n "ffd1Base" -p "upper_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000040E";
	setAttr ".v" no;
	setAttr ".s" -type "double3" 2 9.9999999999999998e-13 0.2 ;
createNode baseLattice -n "ffd1BaseShape" -p "ffd1Base";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000040F";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
createNode transform -n "ffd1Lattice" -p "upper_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000410";
	setAttr ".v" no;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr ".s" -type "double3" 2 9.9999999999999998e-13 0.2 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".it" no;
createNode lattice -n "ffd1LatticeShape" -p "ffd1Lattice";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000411";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".tw" yes;
	setAttr ".sd" 3;
	setAttr ".td" 2;
createNode lattice -n "ffd1LatticeShapeOrig" -p "ffd1Lattice";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000412";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".sd" 3;
	setAttr ".td" 2;
	setAttr ".cc" -type "lattice" 3 2 2 12 -0.5 -0.5 -0.5 0
		 -0.5 -0.5 0.5 -0.5 -0.5 -0.5 0.5 -0.5 0 0.5 -0.5 0.5
		 0.5 -0.5 -0.5 -0.5 0.5 0 -0.5 0.5 0.5 -0.5 0.5 -0.5
		 0.5 0.5 0 0.5 0.5 0.5 0.5 0.5 ;
createNode transform -n "duplicatedCurve1" -p "upper_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000413";
	setAttr ".v" no;
	setAttr ".it" no;
createNode nurbsCurve -n "duplicatedCurveShape1" -p "duplicatedCurve1";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000414";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "duplicatedCurve2" -p "upper_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000415";
	setAttr ".v" no;
	setAttr ".it" no;
createNode nurbsCurve -n "duplicatedCurveShape2" -p "duplicatedCurve2";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000416";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "loftedSurface1" -p "upper_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000417";
	setAttr ".it" no;
createNode nurbsSurface -n "loftedSurfaceShape1" -p "loftedSurface1";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000418";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".tw" yes;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dvu" 0;
	setAttr ".dvv" 0;
	setAttr ".cpr" 4;
	setAttr ".cps" 4;
createNode joint -n "upper_start" -p "cartoony_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000419";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 -1 0 0 1;
	setAttr ".radi" 0.1;
createNode parentConstraint -n "upper_start_parentConstraint1" -p "upper_start";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000041A";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "upper_cartoony_CONW0" -dv 1 -min 
		0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 1.2048681681903391e-16 5.3506895278513982e-32 ;
	setAttr ".rst" -type "double3" -2 4.9303806576313238e-32 5.3506895278513982e-32 ;
	setAttr -k on ".w0";
createNode joint -n "upper_mid" -p "cartoony_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000041B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 0 0 0 1;
	setAttr ".radi" 0.1;
createNode parentConstraint -n "upper_mid_parentConstraint1" -p "upper_mid";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000041C";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "bezierHandleA_CONW0" -dv 1 -min 0 
		-at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 0.024425238370790435 0 ;
	setAttr ".tg[0].tor" -type "double3" 0 0 -180 ;
	setAttr ".rst" -type "double3" -1.2575856020390785 -0.024425238370790435 -5.8964802820329492e-17 ;
	setAttr -k on ".w0";
createNode joint -n "upper_end" -p "cartoony_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000041D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 1 0 0 1;
	setAttr ".radi" 0.1;
createNode parentConstraint -n "upper_end_parentConstraint1" -p "upper_end";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000041E";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "bezier_CONW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 1.7779218543272284e-30 0 -1.776356839400252e-15 ;
	setAttr ".rst" -type "double3" -7.0064923216240854e-46 0 -1.5777218104420236e-30 ;
	setAttr -k on ".w0";
createNode joint -n "lower_mid" -p "cartoony_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000041F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 0 0 0 1;
	setAttr ".radi" 0.1;
createNode parentConstraint -n "lower_mid_parentConstraint1" -p "lower_mid";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000420";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "bezierHandleB_CONW0" -dv 1 -min 0 
		-at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 0.024425238370790425 0 ;
	setAttr ".rst" -type "double3" 1.2575856020390788 0.024425238370790425 -2.8774677577690392e-16 ;
	setAttr -k on ".w0";
createNode joint -n "lower_start" -p "cartoony_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000421";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 -1 0 0 1;
	setAttr ".radi" 0.1;
createNode parentConstraint -n "lower_start_parentConstraint1" -p "lower_start";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000422";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "bezier_CONW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 1.7779218543272288e-30 0 -1.7763568394002513e-15 ;
	setAttr ".rst" -type "double3" -3.5032461608120427e-46 0 -7.8886090522101181e-31 ;
	setAttr -k on ".w0";
createNode joint -n "lower_end" -p "cartoony_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000423";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 1 0 0 1;
	setAttr ".radi" 0.1;
createNode parentConstraint -n "lower_end_parentConstraint1" -p "lower_end";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000424";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "lower_cartoony_CONW0" -dv 1 -min 
		0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 2 0 0 ;
	setAttr -k on ".w0";
createNode transform -n "controls" -p "cartoony_GRP";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000425";
createNode transform -n "upper_cartoony_OFS" -p "controls";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000426";
	setAttr ".t" -type "double3" -2 0 0 ;
createNode transform -n "upper_cartoony_CON" -p "upper_cartoony_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000427";
	setAttr ".t" -type "double3" -5.9164567891575885e-31 -1.2048681681903386e-16 0 ;
createNode nurbsCurve -n "upper_cartoony_CONShape" -p "upper_cartoony_CON";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000428";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 52 0 no 3
		53 0 1 2 3 4 5 6 7 8 9 10
		 11 12 13 14 15 16 17 18 19 20 21 22
		 23 24 25 26 27 28 29 30 31 32 33 34
		 35 36 37 38 39 40 41 42 43 44 45 46
		 47 48 49 50 51 52
		53
		0 0.25965380797563137 0
		0 0.23992011856948317 0.099447408454666805
		0 0.18357524223877145 0.18357524223877145
		0 0.099447408454666805 0.23992011856948317
		0 0 0.25965380797563137
		0 -0.099447408454666805 0.23992011856948317
		0 -0.18357524223877145 0.18357524223877145
		0 -0.23992011856948317 0.099447408454666805
		0 -0.25965380797563137 0
		0 -0.23992011856948317 -0.099447408454666805
		0 -0.18357524223877145 -0.18357524223877145
		0 -0.099447408454666805 -0.23992011856948317
		0 0 -0.25965380797563137
		0 0.099447408454666805 -0.23992011856948317
		0 0.18357524223877145 -0.18357524223877145
		0 0.23992011856948317 -0.099447408454666805
		0 0.25965380797563137 0
		0.099447408454666805 0.23992011856948317 0
		0.18357524223877145 0.18357524223877145 0
		0.23992011856948317 0.099447408454666805 0
		0.25965380797563137 0 0
		0.23992011856948317 -0.099447408454666805 0
		0.18357524223877145 -0.18357524223877145 0
		0.099447408454666805 -0.23992011856948317 0
		0 -0.25965380797563137 0
		-0.099447408454666805 -0.23992011856948317 0
		-0.18357524223877145 -0.18357524223877145 0
		-0.23992011856948317 -0.099447408454666805 0
		-0.25965380797563137 0 0
		-0.23992011856948317 0.099447408454666805 0
		-0.18357524223877145 0.18357524223877145 0
		-0.099447408454666805 0.23992011856948317 0
		0 0.25965380797563137 0
		0 0.23992011856948317 -0.099447408454666805
		0 0.18357524223877145 -0.18357524223877145
		0 0.099447408454666805 -0.23992011856948317
		0 0 -0.25965380797563137
		-0.099447408454666805 0 -0.23992011856948317
		-0.18357524223877145 0 -0.18357524223877145
		-0.23992011856948317 0 -0.099447408454666805
		-0.25965380797563137 0 0
		-0.23992011856948317 0 0.099447408454666805
		-0.18357524223877145 0 0.18357524223877145
		-0.099447408454666805 0 0.23992011856948317
		0 0 0.25965380797563137
		0.099447408454666805 0 0.23992011856948317
		0.18357524223877145 0 0.18357524223877145
		0.23992011856948317 0 0.099447408454666805
		0.25965380797563137 0 0
		0.23992011856948317 0 -0.099447408454666805
		0.18357524223877145 0 -0.18357524223877145
		0.099447408454666805 0 -0.23992011856948317
		0 0 -0.25965380797563137
		;
createNode transform -n "bezier_OFS" -p "controls";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000429";
	setAttr ".t" -type "double3" 0 0 1.7763568394002505e-15 ;
createNode transform -n "bezier_CON" -p "bezier_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000042A";
	setAttr ".t" -type "double3" -1.7779218543272291e-30 0 0 ;
createNode nurbsCurve -n "bezier_CONShape" -p "bezier_CON";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000042B";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 52 0 no 3
		53 0 1 2 3 4 5 6 7 8 9 10
		 11 12 13 14 15 16 17 18 19 20 21 22
		 23 24 25 26 27 28 29 30 31 32 33 34
		 35 36 37 38 39 40 41 42 43 44 45 46
		 47 48 49 50 51 52
		53
		0 0.25965380797563137 0
		0 0.23992011856948317 0.099447408454666805
		0 0.18357524223877145 0.18357524223877145
		0 0.099447408454666805 0.23992011856948317
		0 0 0.25965380797563137
		0 -0.099447408454666805 0.23992011856948317
		0 -0.18357524223877145 0.18357524223877145
		0 -0.23992011856948317 0.099447408454666805
		0 -0.25965380797563137 0
		0 -0.23992011856948317 -0.099447408454666805
		0 -0.18357524223877145 -0.18357524223877145
		0 -0.099447408454666805 -0.23992011856948317
		0 0 -0.25965380797563137
		0 0.099447408454666805 -0.23992011856948317
		0 0.18357524223877145 -0.18357524223877145
		0 0.23992011856948317 -0.099447408454666805
		0 0.25965380797563137 0
		0.099447408454666805 0.23992011856948317 0
		0.18357524223877145 0.18357524223877145 0
		0.23992011856948317 0.099447408454666805 0
		0.25965380797563137 0 0
		0.23992011856948317 -0.099447408454666805 0
		0.18357524223877145 -0.18357524223877145 0
		0.099447408454666805 -0.23992011856948317 0
		0 -0.25965380797563137 0
		-0.099447408454666805 -0.23992011856948317 0
		-0.18357524223877145 -0.18357524223877145 0
		-0.23992011856948317 -0.099447408454666805 0
		-0.25965380797563137 0 0
		-0.23992011856948317 0.099447408454666805 0
		-0.18357524223877145 0.18357524223877145 0
		-0.099447408454666805 0.23992011856948317 0
		0 0.25965380797563137 0
		0 0.23992011856948317 -0.099447408454666805
		0 0.18357524223877145 -0.18357524223877145
		0 0.099447408454666805 -0.23992011856948317
		0 0 -0.25965380797563137
		-0.099447408454666805 0 -0.23992011856948317
		-0.18357524223877145 0 -0.18357524223877145
		-0.23992011856948317 0 -0.099447408454666805
		-0.25965380797563137 0 0
		-0.23992011856948317 0 0.099447408454666805
		-0.18357524223877145 0 0.18357524223877145
		-0.099447408454666805 0 0.23992011856948317
		0 0 0.25965380797563137
		0.099447408454666805 0 0.23992011856948317
		0.18357524223877145 0 0.18357524223877145
		0.23992011856948317 0 0.099447408454666805
		0.25965380797563137 0 0
		0.23992011856948317 0 -0.099447408454666805
		0.18357524223877145 0 -0.18357524223877145
		0.099447408454666805 0 -0.23992011856948317
		0 0 -0.25965380797563137
		;
createNode transform -n "bezierHandleA_OFS" -p "bezier_CON";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000042C";
	setAttr ".t" -type "double3" -1.2575856020390785 0 -1.8353216422205801e-15 ;
	setAttr ".r" -type "double3" 0 0 180 ;
createNode transform -n "bezierHandleA_CON" -p "bezierHandleA_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000042D";
	setAttr ".t" -type "double3" 0 0 9.8607613152626476e-32 ;
createNode nurbsCurve -n "bezierHandleA_CONShape" -p "bezierHandleA_CON";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000042E";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10
		 11 12 13 14 15 16
		17
		-0.051930761595126308 0.051930761595126308 0.051930761595126308
		-0.051930761595126308 0.051930761595126308 -0.051930761595126308
		0.051930761595126308 0.051930761595126308 -0.051930761595126308
		0.051930761595126308 0.051930761595126308 0.051930761595126308
		-0.051930761595126308 0.051930761595126308 0.051930761595126308
		-0.051930761595126308 -0.051930761595126308 0.051930761595126308
		-0.051930761595126308 -0.051930761595126308 -0.051930761595126308
		-0.051930761595126308 0.051930761595126308 -0.051930761595126308
		-0.051930761595126308 0.051930761595126308 0.051930761595126308
		-0.051930761595126308 -0.051930761595126308 0.051930761595126308
		0.051930761595126308 -0.051930761595126308 0.051930761595126308
		0.051930761595126308 0.051930761595126308 0.051930761595126308
		0.051930761595126308 0.051930761595126308 -0.051930761595126308
		0.051930761595126308 -0.051930761595126308 -0.051930761595126308
		0.051930761595126308 -0.051930761595126308 0.051930761595126308
		0.051930761595126308 -0.051930761595126308 -0.051930761595126308
		-0.051930761595126308 -0.051930761595126308 -0.051930761595126308
		;
createNode transform -n "a_line" -p "bezierHandleA_CON";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000042F";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".it" no;
createNode nurbsCurve -n "a_lineShape" -p "a_line";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000430";
	setAttr -k off ".v";
	setAttr -s 2 ".cp";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		-1.2575856020390785 0 -5.8964802820329492e-17
		-1.7779218543272291e-30 0 1.7763568394002505e-15
		;
createNode transform -n "bezierHandleB_OFS" -p "bezier_CON";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000431";
	setAttr ".t" -type "double3" 1.2575856020390788 0 -2.0641036151771544e-15 ;
createNode transform -n "bezierHandleB_CON" -p "bezierHandleB_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000432";
createNode nurbsCurve -n "bezierHandleB_CON0Shape" -p "bezierHandleB_CON";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000433";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 16;
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10
		 11 12 13 14 15 16
		17
		-0.051930761595126308 0.051930761595126308 0.051930761595126308
		-0.051930761595126308 0.051930761595126308 -0.051930761595126308
		0.051930761595126308 0.051930761595126308 -0.051930761595126308
		0.051930761595126308 0.051930761595126308 0.051930761595126308
		-0.051930761595126308 0.051930761595126308 0.051930761595126308
		-0.051930761595126308 -0.051930761595126308 0.051930761595126308
		-0.051930761595126308 -0.051930761595126308 -0.051930761595126308
		-0.051930761595126308 0.051930761595126308 -0.051930761595126308
		-0.051930761595126308 0.051930761595126308 0.051930761595126308
		-0.051930761595126308 -0.051930761595126308 0.051930761595126308
		0.051930761595126308 -0.051930761595126308 0.051930761595126308
		0.051930761595126308 0.051930761595126308 0.051930761595126308
		0.051930761595126308 0.051930761595126308 -0.051930761595126308
		0.051930761595126308 -0.051930761595126308 -0.051930761595126308
		0.051930761595126308 -0.051930761595126308 0.051930761595126308
		0.051930761595126308 -0.051930761595126308 -0.051930761595126308
		-0.051930761595126308 -0.051930761595126308 -0.051930761595126308
		;
createNode transform -n "b_line" -p "bezierHandleB_CON";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000434";
	setAttr ".ovdt" 1;
	setAttr ".ove" yes;
	setAttr ".it" no;
createNode nurbsCurve -n "b_line0Shape" -p "b_line";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000435";
	setAttr -k off ".v";
	setAttr -s 2 ".cp";
	setAttr ".cc" -type "nurbsCurve" 
		1 1 0 no 3
		2 0 1
		2
		1.2575856020390788 0 -2.8774677577690392e-16
		-1.7779218543272291e-30 0 1.7763568394002505e-15
		;
createNode transform -n "lower_cartoony_OFS" -p "controls";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000436";
	setAttr ".t" -type "double3" 2 0 0 ;
createNode transform -n "lower_cartoony_CON" -p "lower_cartoony_OFS";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000437";
createNode nurbsCurve -n "lower_cartoony_CON1Shape" -p "lower_cartoony_CON";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000438";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 52 0 no 3
		53 0 1 2 3 4 5 6 7 8 9 10
		 11 12 13 14 15 16 17 18 19 20 21 22
		 23 24 25 26 27 28 29 30 31 32 33 34
		 35 36 37 38 39 40 41 42 43 44 45 46
		 47 48 49 50 51 52
		53
		0 0.25965380797563137 0
		0 0.23992011856948317 0.099447408454666805
		0 0.18357524223877145 0.18357524223877145
		0 0.099447408454666805 0.23992011856948317
		0 0 0.25965380797563137
		0 -0.099447408454666805 0.23992011856948317
		0 -0.18357524223877145 0.18357524223877145
		0 -0.23992011856948317 0.099447408454666805
		0 -0.25965380797563137 0
		0 -0.23992011856948317 -0.099447408454666805
		0 -0.18357524223877145 -0.18357524223877145
		0 -0.099447408454666805 -0.23992011856948317
		0 0 -0.25965380797563137
		0 0.099447408454666805 -0.23992011856948317
		0 0.18357524223877145 -0.18357524223877145
		0 0.23992011856948317 -0.099447408454666805
		0 0.25965380797563137 0
		0.099447408454666805 0.23992011856948317 0
		0.18357524223877145 0.18357524223877145 0
		0.23992011856948317 0.099447408454666805 0
		0.25965380797563137 0 0
		0.23992011856948317 -0.099447408454666805 0
		0.18357524223877145 -0.18357524223877145 0
		0.099447408454666805 -0.23992011856948317 0
		0 -0.25965380797563137 0
		-0.099447408454666805 -0.23992011856948317 0
		-0.18357524223877145 -0.18357524223877145 0
		-0.23992011856948317 -0.099447408454666805 0
		-0.25965380797563137 0 0
		-0.23992011856948317 0.099447408454666805 0
		-0.18357524223877145 0.18357524223877145 0
		-0.099447408454666805 0.23992011856948317 0
		0 0.25965380797563137 0
		0 0.23992011856948317 -0.099447408454666805
		0 0.18357524223877145 -0.18357524223877145
		0 0.099447408454666805 -0.23992011856948317
		0 0 -0.25965380797563137
		-0.099447408454666805 0 -0.23992011856948317
		-0.18357524223877145 0 -0.18357524223877145
		-0.23992011856948317 0 -0.099447408454666805
		-0.25965380797563137 0 0
		-0.23992011856948317 0 0.099447408454666805
		-0.18357524223877145 0 0.18357524223877145
		-0.099447408454666805 0 0.23992011856948317
		0 0 0.25965380797563137
		0.099447408454666805 0 0.23992011856948317
		0.18357524223877145 0 0.18357524223877145
		0.23992011856948317 0 0.099447408454666805
		0.25965380797563137 0 0
		0.23992011856948317 0 -0.099447408454666805
		0.18357524223877145 0 -0.18357524223877145
		0.099447408454666805 0 -0.23992011856948317
		0 0 -0.25965380797563137
		;
createNode transform -n "pCylinder1";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000439";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode mesh -n "pCylinderShape1" -p "pCylinder1";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000043A";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".ndt" 0;
	setAttr ".vcs" 2;
createNode mesh -n "pCylinderShape1Orig" -p "pCylinder1";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000043B";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".ndt" 0;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000387";
	setAttr -s 5 ".lnk";
	setAttr -s 5 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000388";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000389";
createNode displayLayerManager -n "layerManager";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000038A";
createNode displayLayer -n "defaultLayer";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000038B";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000038C";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000038D";
	setAttr ".g" yes;
createNode ikSCsolver -n "ikSCsolver";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003B0";
createNode clamp -n "test_slide_shift_clamp";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003B1";
	setAttr ".mx" -type "float3" 1 0 0 ;
createNode multDoubleLinear -n "test_slide_shift_mdl";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003B2";
	setAttr ".i1" 1;
createNode cluster -n "cluster5";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003B3";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 0 0 0 1;
createNode tweak -n "tweak2";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003B4";
createNode objectSet -n "cluster5Set";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003B5";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "cluster5GroupId";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003B6";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster5GroupParts";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003B7";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[0]";
createNode objectSet -n "tweakSet2";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003B8";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId4";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003B9";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts4";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003BA";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*]";
createNode wtAddMatrix -n "test_bm_010";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003BB";
	setAttr -s 2 ".i";
	setAttr ".i[0].w" 0.52631578947368429;
	setAttr ".i[1].w" 0.47368421052631576;
createNode pointMatrixMult -n "test_up_pmm_010";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003BC";
	setAttr ".ip" -type "double3" 0 100 0 ;
	setAttr ".vm" yes;
createNode decomposeMatrix -n "test_up_dm_010";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003BD";
createNode plusMinusAverage -n "test_up_pma_010";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003BE";
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode pointOnCurveInfo -n "test_poc_010";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003BF";
	setAttr ".pr" 0.5;
	setAttr ".top" yes;
createNode plusMinusAverage -n "test_pma_010";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003C0";
	setAttr ".op" 2;
	setAttr -s 2 ".i3";
	setAttr -s 2 ".i3";
createNode clamp -n "test_slide_shift_clamp1";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003C1";
	setAttr ".mx" -type "float3" 1 0 0 ;
createNode multDoubleLinear -n "test_slide_shift_mdl1";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003C2";
	setAttr ".i1" 1;
createNode clamp -n "test_slide_shift_min_clamp";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003C3";
	setAttr ".mx" -type "float3" 1 0 0 ;
createNode clamp -n "test_slide_shift_max_clamp";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003C4";
	setAttr ".mx" -type "float3" 1 0 0 ;
createNode ramp -n "test_slide_ramp_009";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003C5";
	setAttr -s 3 ".cel";
	setAttr ".cel[0].ec" -type "float3" 0 0 0 ;
	setAttr ".cel[1].ec" -type "float3" 0 1 1 ;
	setAttr ".cel[2].ec" -type "float3" 0.5 0.5 0.5 ;
createNode addDoubleLinear -n "test_slide_uv_adl_009";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003C6";
	setAttr ".i2" 0.47368421052631576;
createNode condition -n "test_slide_cd_a_009";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003C7";
	setAttr ".op" 5;
	setAttr ".st" 0.47368422150611877;
	setAttr ".ct" -type "float3" 1 0 0 ;
	setAttr ".cf" -type "float3" 0 1 1 ;
createNode condition -n "test_slide_cd_b_009";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003C8";
	setAttr ".op" 3;
	setAttr ".st" 0.47368422150611877;
	setAttr ".ct" -type "float3" 1 0 0 ;
	setAttr ".cf" -type "float3" 0 1 1 ;
createNode multDoubleLinear -n "test_slide_mdl_009";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003C9";
createNode condition -n "test_slide_cd_c_009";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003CA";
	setAttr ".ct" -type "float3" 0.47368422 0 0 ;
createNode cluster -n "cluster6";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003CB";
	setAttr ".gm[0]" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 0 0 0 1;
createNode objectSet -n "cluster6Set";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003CC";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "cluster6GroupId";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003CD";
	setAttr ".ihi" 0;
createNode groupParts -n "cluster6GroupParts";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003CE";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[1]";
createNode script -n "uiConfigurationScriptNode";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003CF";
	setAttr ".b" -type "string" "// Maya Mel UI Configuration File.\n// No UI generated in batch mode.\n";
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003D0";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000003D1";
	setAttr ".def" no;
	setAttr -s 2 ".tgi";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -199.58790415700119 1516.6666063997602 ;
	setAttr ".tgi[0].vh" -type "double2" 4024.5877521651632 2660.7141799870133 ;
	setAttr ".tgi[0].ni[0].x" 1658.4417724609375;
	setAttr ".tgi[0].ni[0].y" 1899.673583984375;
	setAttr ".tgi[0].ni[0].nvs" 18305;
	setAttr ".tgi[1].tn" -type "string" "Untitled_2";
	setAttr ".tgi[1].vl" -type "double2" 143.26922507622319 -40.476188867813633 ;
	setAttr ".tgi[1].vh" -type "double2" 4367.4448813983881 1103.5713847194393 ;
	setAttr -s 29 ".tgi[1].ni";
	setAttr ".tgi[1].ni[0].x" 2927.142822265625;
	setAttr ".tgi[1].ni[0].y" 677.14288330078125;
	setAttr ".tgi[1].ni[0].nvs" 18305;
	setAttr ".tgi[1].ni[1].x" 2312.857177734375;
	setAttr ".tgi[1].ni[1].y" 777.14288330078125;
	setAttr ".tgi[1].ni[1].nvs" 18305;
	setAttr ".tgi[1].ni[2].x" 518.5714111328125;
	setAttr ".tgi[1].ni[2].y" 541.4285888671875;
	setAttr ".tgi[1].ni[2].nvs" 18304;
	setAttr ".tgi[1].ni[3].x" 3887.142822265625;
	setAttr ".tgi[1].ni[3].y" 541.4285888671875;
	setAttr ".tgi[1].ni[3].nvs" 18304;
	setAttr ".tgi[1].ni[4].x" 1391.4285888671875;
	setAttr ".tgi[1].ni[4].y" 547.14288330078125;
	setAttr ".tgi[1].ni[4].nvs" 18304;
	setAttr ".tgi[1].ni[5].x" 1084.2857666015625;
	setAttr ".tgi[1].ni[5].y" 498.57144165039062;
	setAttr ".tgi[1].ni[5].nvs" 18304;
	setAttr ".tgi[1].ni[6].x" 2680;
	setAttr ".tgi[1].ni[6].y" -91.428573608398438;
	setAttr ".tgi[1].ni[6].nvs" 18304;
	setAttr ".tgi[1].ni[7].x" 1544.2857666015625;
	setAttr ".tgi[1].ni[7].y" 884.28570556640625;
	setAttr ".tgi[1].ni[7].nvs" 18304;
	setAttr ".tgi[1].ni[8].x" 2160;
	setAttr ".tgi[1].ni[8].y" 974.28570556640625;
	setAttr ".tgi[1].ni[8].nvs" 18304;
	setAttr ".tgi[1].ni[9].x" 2372.857177734375;
	setAttr ".tgi[1].ni[9].y" 261.42855834960938;
	setAttr ".tgi[1].ni[9].nvs" 18304;
	setAttr ".tgi[1].ni[10].x" 1391.4285888671875;
	setAttr ".tgi[1].ni[10].y" 448.57144165039062;
	setAttr ".tgi[1].ni[10].nvs" 18304;
	setAttr ".tgi[1].ni[11].x" 1698.5714111328125;
	setAttr ".tgi[1].ni[11].y" 400;
	setAttr ".tgi[1].ni[11].nvs" 18304;
	setAttr ".tgi[1].ni[12].x" 2005.7142333984375;
	setAttr ".tgi[1].ni[12].y" 547.14288330078125;
	setAttr ".tgi[1].ni[12].nvs" 18304;
	setAttr ".tgi[1].ni[13].x" 2005.7142333984375;
	setAttr ".tgi[1].ni[13].y" 350;
	setAttr ".tgi[1].ni[13].nvs" 18304;
	setAttr ".tgi[1].ni[14].x" 3234.28564453125;
	setAttr ".tgi[1].ni[14].y" 705.71429443359375;
	setAttr ".tgi[1].ni[14].nvs" 18306;
	setAttr ".tgi[1].ni[15].x" 1394.2857666015625;
	setAttr ".tgi[1].ni[15].y" 1072.857177734375;
	setAttr ".tgi[1].ni[15].nvs" 18304;
	setAttr ".tgi[1].ni[16].x" 2680;
	setAttr ".tgi[1].ni[16].y" 212.85714721679688;
	setAttr ".tgi[1].ni[16].nvs" 18304;
	setAttr ".tgi[1].ni[17].x" 3887.142822265625;
	setAttr ".tgi[1].ni[17].y" 414.28570556640625;
	setAttr ".tgi[1].ni[17].nvs" 18304;
	setAttr ".tgi[1].ni[18].x" 518.5714111328125;
	setAttr ".tgi[1].ni[18].y" 414.28570556640625;
	setAttr ".tgi[1].ni[18].nvs" 18304;
	setAttr ".tgi[1].ni[19].x" 1698.5714111328125;
	setAttr ".tgi[1].ni[19].y" 518.5714111328125;
	setAttr ".tgi[1].ni[19].nvs" 18304;
	setAttr ".tgi[1].ni[20].x" 2924.28564453125;
	setAttr ".tgi[1].ni[20].y" 1072.857177734375;
	setAttr ".tgi[1].ni[20].nvs" 18304;
	setAttr ".tgi[1].ni[21].x" 2680;
	setAttr ".tgi[1].ni[21].y" 35.714286804199219;
	setAttr ".tgi[1].ni[21].nvs" 18304;
	setAttr ".tgi[1].ni[22].x" 2312.857177734375;
	setAttr ".tgi[1].ni[22].y" 464.28570556640625;
	setAttr ".tgi[1].ni[22].nvs" 18304;
	setAttr ".tgi[1].ni[23].x" 2372.857177734375;
	setAttr ".tgi[1].ni[23].y" 162.85714721679688;
	setAttr ".tgi[1].ni[23].nvs" 18304;
	setAttr ".tgi[1].ni[24].x" 2005.7142333984375;
	setAttr ".tgi[1].ni[24].y" 448.57144165039062;
	setAttr ".tgi[1].ni[24].nvs" 18304;
	setAttr ".tgi[1].ni[25].x" 2620;
	setAttr ".tgi[1].ni[25].y" 585.71429443359375;
	setAttr ".tgi[1].ni[25].nvs" 18304;
	setAttr ".tgi[1].ni[26].x" 1391.4285888671875;
	setAttr ".tgi[1].ni[26].y" 350;
	setAttr ".tgi[1].ni[26].nvs" 18304;
	setAttr ".tgi[1].ni[27].x" 1084.2857666015625;
	setAttr ".tgi[1].ni[27].y" 597.14288330078125;
	setAttr ".tgi[1].ni[27].nvs" 18304;
	setAttr ".tgi[1].ni[28].x" 1534.2857666015625;
	setAttr ".tgi[1].ni[28].y" 834.28570556640625;
	setAttr ".tgi[1].ni[28].nvs" 18304;
createNode lambert -n "lambert2";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000445";
	setAttr ".c" -type "float3" 0 0 1 ;
createNode shadingEngine -n "lambert2SG";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000446";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo1";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000447";
createNode lambert -n "lambert3";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000448";
	setAttr ".c" -type "float3" 1 0 0 ;
createNode shadingEngine -n "lambert3SG";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000449";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo2";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000044A";
createNode lambert -n "lambert4";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000044B";
	setAttr ".c" -type "float3" 0 1 0 ;
createNode shadingEngine -n "lambert4SG";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000044C";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo3";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000044D";
createNode remapValue -n "slide_RMP1";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000044E";
	setAttr ".imx" 10;
	setAttr -s 2 ".vl[0:1]"  0 0 1 1 1 1;
	setAttr -s 2 ".cl";
	setAttr ".cl[0].clp" 0;
	setAttr ".cl[0].clc" -type "float3" 0 0 0 ;
	setAttr ".cl[0].cli" 1;
	setAttr ".cl[1].clp" 1;
	setAttr ".cl[1].clc" -type "float3" 1 1 1 ;
	setAttr ".cl[1].cli" 1;
createNode tweak -n "tweak1";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000044F";
createNode groupParts -n "groupParts18";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000450";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*][*]";
createNode groupId -n "groupId21";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000451";
	setAttr ".ihi" 0;
createNode objectSet -n "tweakSet1";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000452";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode makeNurbPlane -n "makeNurbPlane1";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000453";
	setAttr ".ax" -type "double3" 0 1 0 ;
	setAttr ".w" 2;
	setAttr ".lr" 0.1;
	setAttr ".u" 20;
createNode ffd -n "ffd1";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000454";
createNode objectSet -n "ffd1Set";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000455";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "ffd1GroupId";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000456";
	setAttr ".ihi" 0;
createNode groupParts -n "ffd1GroupParts";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000457";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*][*]";
createNode skinCluster -n "skinCluster1";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000458";
	setAttr -s 12 ".wl";
	setAttr ".wl[0:11].w"
		2 0 0.99990198000392083 1 9.8019996079200226e-05
		2 0 9.8019996079200226e-05 1 0.99990198000392083
		2 1 9.8019996079200226e-05 2 0.99990198000392083
		2 0 0.99990198000392083 1 9.8019996079200226e-05
		2 0 9.8019996079200226e-05 1 0.99990198000392083
		2 1 9.8019996079200226e-05 2 0.99990198000392083
		2 0 0.99990198000392083 1 9.8019996079200226e-05
		2 0 9.8019996079200226e-05 1 0.99990198000392083
		2 1 9.8019996079200226e-05 2 0.99990198000392083
		2 0 0.99990198000392083 1 9.8019996079200226e-05
		2 0 9.8019996079200226e-05 1 0.99990198000392083
		2 1 9.8019996079200226e-05 2 0.99990198000392083;
	setAttr -s 3 ".pm";
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 1 0 0 1;
	setAttr ".pm[1]" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 0 0 0 1;
	setAttr ".pm[2]" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 -1 0 0 1;
	setAttr ".gm" -type "matrix" 2 0 0 0 0 9.9999999999999998e-13 0 0
		 0 0 0.20000000000000001 0 0 0 0 1;
	setAttr -s 3 ".ma";
	setAttr -s 3 ".dpf[0:2]"  4 4 4;
	setAttr -s 3 ".lw";
	setAttr -s 3 ".lw";
	setAttr ".mmi" yes;
	setAttr ".ucm" yes;
	setAttr -s 3 ".ifcl";
	setAttr -s 3 ".ifcl";
createNode tweak -n "tweak3";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000459";
createNode objectSet -n "skinCluster1Set";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000045A";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster1GroupId";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000045B";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster1GroupParts";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000045C";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "pt[*][*][*]";
createNode objectSet -n "tweakSet3";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000045D";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId23";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000045E";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts20";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000045F";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "pt[*][*][*]";
createNode dagPose -n "bindPose1";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000460";
	setAttr -s 3 ".wm";
	setAttr -s 3 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 -1
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[2]" -type "matrix" "xform" 1 1 1 0 0 0 0 1
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr -s 3 ".m";
	setAttr -s 3 ".p";
	setAttr ".bp" yes;
createNode curveFromSurfaceIso -n "curveFromSurfaceIso1";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000461";
	setAttr ".ihi" 1;
	setAttr ".max" 0;
	setAttr ".iv" 1;
createNode curveFromSurfaceIso -n "curveFromSurfaceIso2";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000462";
	setAttr ".ihi" 1;
	setAttr ".max" 0;
createNode rebuildCurve -n "rebuildCurve1";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000463";
	setAttr ".s" 40;
createNode rebuildCurve -n "rebuildCurve2";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000464";
	setAttr ".s" 40;
createNode loft -n "loft1";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000465";
	setAttr -s 2 ".ic";
	setAttr ".u" yes;
	setAttr ".rsn" yes;
createNode rebuildSurface -n "rebuildSurface1";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000466";
	setAttr ".rt" 7;
	setAttr ".su" 0;
	setAttr ".sv" 0;
	setAttr ".du" 0;
	setAttr ".dv" 0;
createNode decomposeMatrix -n "decompose_mtx_NOD2";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000467";
createNode fourByFourMatrix -n "compose_mtx_NOD2";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000468";
createNode pointOnSurfaceInfo -n "xy_axis_NOD2";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000469";
	setAttr ".v" 0.5;
createNode remapValue -n "slide_RMP2";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000046A";
	setAttr ".imx" 10;
	setAttr -s 2 ".vl[0:1]"  0 0 1 1 1 1;
	setAttr -s 2 ".cl";
	setAttr ".cl[0].clp" 0;
	setAttr ".cl[0].clc" -type "float3" 0 0 0 ;
	setAttr ".cl[0].cli" 1;
	setAttr ".cl[1].clp" 1;
	setAttr ".cl[1].clc" -type "float3" 1 1 1 ;
	setAttr ".cl[1].cli" 1;
createNode vectorProduct -n "z_axis_NOD2";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000046B";
	setAttr ".op" 2;
createNode decomposeMatrix -n "decompose_mtx_NOD3";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000046C";
createNode fourByFourMatrix -n "compose_mtx_NOD3";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000046D";
createNode pointOnSurfaceInfo -n "xy_axis_NOD3";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000046E";
	setAttr ".v" 0.5;
createNode vectorProduct -n "z_axis_NOD3";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000046F";
	setAttr ".op" 2;
createNode decomposeMatrix -n "decompose_mtx_NOD4";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000470";
createNode fourByFourMatrix -n "compose_mtx_NOD4";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000471";
createNode pointOnSurfaceInfo -n "xy_axis_NOD4";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000472";
	setAttr ".v" 0.5;
createNode vectorProduct -n "z_axis_NOD4";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000473";
	setAttr ".op" 2;
createNode decomposeMatrix -n "decompose_mtx_NOD5";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000474";
createNode fourByFourMatrix -n "compose_mtx_NOD5";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000475";
createNode pointOnSurfaceInfo -n "xy_axis_NOD5";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000476";
	setAttr ".v" 0.5;
createNode vectorProduct -n "z_axis_NOD5";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000477";
	setAttr ".op" 2;
createNode decomposeMatrix -n "decompose_mtx_NOD6";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000478";
createNode fourByFourMatrix -n "compose_mtx_NOD6";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000479";
createNode pointOnSurfaceInfo -n "xy_axis_NOD6";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000047A";
	setAttr ".v" 0.5;
createNode vectorProduct -n "z_axis_NOD6";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000047B";
	setAttr ".op" 2;
createNode decomposeMatrix -n "decompose_mtx_NOD7";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000047C";
createNode fourByFourMatrix -n "compose_mtx_NOD7";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000047D";
createNode pointOnSurfaceInfo -n "xy_axis_NOD7";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000047E";
	setAttr ".v" 0.5;
createNode vectorProduct -n "z_axis_NOD7";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000047F";
	setAttr ".op" 2;
createNode decomposeMatrix -n "decompose_mtx_NOD8";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000480";
createNode fourByFourMatrix -n "compose_mtx_NOD8";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000481";
createNode pointOnSurfaceInfo -n "xy_axis_NOD8";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000482";
	setAttr ".v" 0.5;
createNode vectorProduct -n "z_axis_NOD8";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000483";
	setAttr ".op" 2;
createNode decomposeMatrix -n "decompose_mtx_NOD9";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000484";
createNode fourByFourMatrix -n "compose_mtx_NOD9";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000485";
createNode pointOnSurfaceInfo -n "xy_axis_NOD9";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000486";
	setAttr ".v" 0.5;
createNode vectorProduct -n "z_axis_NOD9";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000487";
	setAttr ".op" 2;
createNode decomposeMatrix -n "decompose_mtx_NOD10";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000488";
createNode fourByFourMatrix -n "compose_mtx_NOD10";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000489";
createNode pointOnSurfaceInfo -n "xy_axis_NOD10";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000048A";
	setAttr ".v" 0.5;
createNode vectorProduct -n "z_axis_NOD10";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000048B";
	setAttr ".op" 2;
createNode decomposeMatrix -n "decompose_mtx_NOD11";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000048C";
createNode fourByFourMatrix -n "compose_mtx_NOD11";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000048D";
createNode pointOnSurfaceInfo -n "xy_axis_NOD11";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000048E";
	setAttr ".v" 0.5;
createNode vectorProduct -n "z_axis_NOD11";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000048F";
	setAttr ".op" 2;
createNode remapValue -n "remapValue1";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000490";
	setAttr -s 10 ".vl[0:9]"  0 0 1 0.11111111 0.11111111 1 0.22222222
		 0.22222222 1 0.33333334 0.33333334 1 0.44444445 0.44444445 1 0.55555558
		 0.55555558 1 0.66666669 0.66666669 1 0.77777779 0.77777779 1 0.8888889 0.8888889 
		1 1 1 1;
	setAttr -s 10 ".vl";
	setAttr -s 2 ".cl";
	setAttr ".cl[0].clp" 0;
	setAttr ".cl[0].clc" -type "float3" 0 0 0 ;
	setAttr ".cl[0].cli" 1;
	setAttr ".cl[1].clp" 1;
	setAttr ".cl[1].clc" -type "float3" 1 1 1 ;
	setAttr ".cl[1].cli" 1;
createNode decomposeMatrix -n "decompose_mtx_NOD12";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000491";
createNode fourByFourMatrix -n "compose_mtx_NOD12";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000492";
createNode pointOnSurfaceInfo -n "xy_axis_NOD12";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000493";
	setAttr ".v" 0.5;
createNode remapValue -n "remapValue2";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000494";
	setAttr -s 10 ".vl[0:9]"  0 0 1 0.11111111 0.11111111 1 0.22222222
		 0.22222222 1 0.33333334 0.33333334 1 0.44444445 0.44444445 1 0.55555558
		 0.55555558 1 0.66666669 0.66666669 1 0.77777779 0.77777779 1 0.8888889 0.8888889 
		1 1 1 1;
	setAttr -s 10 ".vl";
	setAttr -s 2 ".cl";
	setAttr ".cl[0].clp" 0;
	setAttr ".cl[0].clc" -type "float3" 0 0 0 ;
	setAttr ".cl[0].cli" 1;
	setAttr ".cl[1].clp" 1;
	setAttr ".cl[1].clc" -type "float3" 1 1 1 ;
	setAttr ".cl[1].cli" 1;
createNode rebuildSurface -n "rebuildSurface2";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000495";
	setAttr ".rt" 7;
	setAttr ".su" 0;
	setAttr ".sv" 0;
	setAttr ".du" 0;
	setAttr ".dv" 0;
createNode loft -n "loft2";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000496";
	setAttr -s 2 ".ic";
	setAttr ".u" yes;
	setAttr ".rsn" yes;
createNode rebuildCurve -n "rebuildCurve3";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000497";
	setAttr ".s" 40;
createNode curveFromSurfaceIso -n "curveFromSurfaceIso3";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000498";
	setAttr ".ihi" 1;
	setAttr ".max" 0;
createNode objectSet -n "tweakSet4";
	rename -uid "7A4DA740-0000-0007-5F43-61A100000499";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId24";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000049A";
	setAttr ".ihi" 0;
createNode tweak -n "tweak4";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000049B";
createNode groupParts -n "groupParts21";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000049C";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*][*]";
createNode makeNurbPlane -n "makeNurbPlane2";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000049D";
	setAttr ".ax" -type "double3" 0 1 0 ;
	setAttr ".w" 2;
	setAttr ".lr" 0.1;
	setAttr ".u" 20;
createNode objectSet -n "ffd1Set1";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000049E";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "ffd1GroupId1";
	rename -uid "7A4DA740-0000-0007-5F43-61A10000049F";
	setAttr ".ihi" 0;
createNode ffd -n "ffd2";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004A0";
createNode skinCluster -n "skinCluster2";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004A1";
	setAttr -s 12 ".wl";
	setAttr ".wl[0:11].w"
		2 0 0.99990198000392083 1 9.8019996079200226e-05
		2 0 9.8019996079200226e-05 1 0.99990198000392083
		2 1 9.8019996079200226e-05 2 0.99990198000392083
		2 0 0.99990198000392083 1 9.8019996079200226e-05
		2 0 9.8019996079200226e-05 1 0.99990198000392083
		2 1 9.8019996079200226e-05 2 0.99990198000392083
		2 0 0.99990198000392083 1 9.8019996079200226e-05
		2 0 9.8019996079200226e-05 1 0.99990198000392083
		2 1 9.8019996079200226e-05 2 0.99990198000392083
		2 0 0.99990198000392083 1 9.8019996079200226e-05
		2 0 9.8019996079200226e-05 1 0.99990198000392083
		2 1 9.8019996079200226e-05 2 0.99990198000392083;
	setAttr -s 3 ".pm";
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 1 0 0 1;
	setAttr ".pm[1]" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 0 0 0 1;
	setAttr ".pm[2]" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 -1 0 0 1;
	setAttr ".gm" -type "matrix" 2 0 0 0 0 9.9999999999999998e-13 0 0
		 0 0 0.20000000000000001 0 0 0 0 1;
	setAttr -s 3 ".ma";
	setAttr -s 3 ".dpf[0:2]"  4 4 4;
	setAttr -s 3 ".lw";
	setAttr -s 3 ".lw";
	setAttr ".mmi" yes;
	setAttr ".ucm" yes;
	setAttr -s 3 ".ifcl";
	setAttr -s 3 ".ifcl";
createNode dagPose -n "bindPose2";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004A2";
	setAttr -s 3 ".wm";
	setAttr -s 3 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 -1
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[2]" -type "matrix" "xform" 1 1 1 0 0 0 0 1
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr -s 3 ".m";
	setAttr -s 3 ".p";
	setAttr ".bp" yes;
createNode objectSet -n "skinCluster1Set1";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004A3";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster1GroupId1";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004A4";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster1GroupParts1";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004A5";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "pt[*][*][*]";
createNode tweak -n "tweak5";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004A6";
createNode objectSet -n "tweakSet5";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004A7";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId25";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004A8";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts22";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004A9";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "pt[*][*][*]";
createNode groupParts -n "ffd1GroupParts1";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004AA";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*][*]";
createNode rebuildCurve -n "rebuildCurve4";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004AB";
	setAttr ".s" 40;
createNode curveFromSurfaceIso -n "curveFromSurfaceIso4";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004AC";
	setAttr ".ihi" 1;
	setAttr ".max" 0;
	setAttr ".iv" 1;
createNode vectorProduct -n "z_axis_NOD12";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004AD";
	setAttr ".op" 2;
createNode decomposeMatrix -n "decompose_mtx_NOD13";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004AE";
createNode fourByFourMatrix -n "compose_mtx_NOD13";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004AF";
createNode pointOnSurfaceInfo -n "xy_axis_NOD13";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004B0";
	setAttr ".v" 0.5;
createNode vectorProduct -n "z_axis_NOD13";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004B1";
	setAttr ".op" 2;
createNode decomposeMatrix -n "decompose_mtx_NOD14";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004B2";
createNode fourByFourMatrix -n "compose_mtx_NOD14";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004B3";
createNode pointOnSurfaceInfo -n "xy_axis_NOD14";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004B4";
	setAttr ".v" 0.5;
createNode vectorProduct -n "z_axis_NOD14";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004B5";
	setAttr ".op" 2;
createNode decomposeMatrix -n "decompose_mtx_NOD15";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004B6";
createNode fourByFourMatrix -n "compose_mtx_NOD15";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004B7";
createNode pointOnSurfaceInfo -n "xy_axis_NOD15";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004B8";
	setAttr ".v" 0.5;
createNode vectorProduct -n "z_axis_NOD15";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004B9";
	setAttr ".op" 2;
createNode decomposeMatrix -n "decompose_mtx_NOD16";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004BA";
createNode fourByFourMatrix -n "compose_mtx_NOD16";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004BB";
createNode pointOnSurfaceInfo -n "xy_axis_NOD16";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004BC";
	setAttr ".v" 0.5;
createNode vectorProduct -n "z_axis_NOD16";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004BD";
	setAttr ".op" 2;
createNode decomposeMatrix -n "decompose_mtx_NOD17";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004BE";
createNode fourByFourMatrix -n "compose_mtx_NOD17";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004BF";
createNode pointOnSurfaceInfo -n "xy_axis_NOD17";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004C0";
	setAttr ".v" 0.5;
createNode vectorProduct -n "z_axis_NOD17";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004C1";
	setAttr ".op" 2;
createNode decomposeMatrix -n "decompose_mtx_NOD18";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004C2";
createNode fourByFourMatrix -n "compose_mtx_NOD18";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004C3";
createNode pointOnSurfaceInfo -n "xy_axis_NOD18";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004C4";
	setAttr ".v" 0.5;
createNode vectorProduct -n "z_axis_NOD18";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004C5";
	setAttr ".op" 2;
createNode decomposeMatrix -n "decompose_mtx_NOD19";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004C6";
createNode fourByFourMatrix -n "compose_mtx_NOD19";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004C7";
createNode pointOnSurfaceInfo -n "xy_axis_NOD19";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004C8";
	setAttr ".v" 0.5;
createNode vectorProduct -n "z_axis_NOD19";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004C9";
	setAttr ".op" 2;
createNode decomposeMatrix -n "decompose_mtx_NOD20";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004CA";
createNode fourByFourMatrix -n "compose_mtx_NOD20";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004CB";
createNode pointOnSurfaceInfo -n "xy_axis_NOD20";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004CC";
	setAttr ".v" 0.5;
createNode vectorProduct -n "z_axis_NOD20";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004CD";
	setAttr ".op" 2;
createNode decomposeMatrix -n "decompose_mtx_NOD21";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004CE";
createNode fourByFourMatrix -n "compose_mtx_NOD21";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004CF";
createNode pointOnSurfaceInfo -n "xy_axis_NOD21";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004D0";
	setAttr ".v" 0.5;
createNode vectorProduct -n "z_axis_NOD21";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004D1";
	setAttr ".op" 2;
createNode clamp -n "test_slide_shift_clamp2";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004D2";
	setAttr ".mx" -type "float3" 1 0 0 ;
createNode multDoubleLinear -n "test_slide_shift_mdl2";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004D3";
	setAttr ".i1" 1;
createNode clamp -n "test_slide_shift_ctrl_clamp";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004D4";
	setAttr ".mx" -type "float3" 1 0 0 ;
createNode multDoubleLinear -n "test_slide_shift_ctrl_mdl";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004D5";
	setAttr ".i1" 1;
createNode decomposeMatrix -n "test_a_line_001_dm_002";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004D6";
createNode decomposeMatrix -n "test_a_line_001_dm_001";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004D7";
createNode decomposeMatrix -n "test_b_line_000_dm_003";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004D8";
createNode decomposeMatrix -n "test_a_line_000_dm_002";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004D9";
createNode polyCylinder -n "polyCylinder1";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004DA";
	setAttr ".ax" -type "double3" 1 0 0 ;
	setAttr ".r" 0.1;
	setAttr ".h" 4;
	setAttr ".sa" 3;
	setAttr ".sh" 20;
	setAttr ".sc" 1;
	setAttr ".cuv" 3;
createNode transformGeometry -n "transformGeometry1";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004DB";
	setAttr ".txf" -type "matrix" 1 0 0 0 0 3.3192579409917782 0 0
		 0 0 1 0 0 0 0 1;
createNode skinCluster -n "skinCluster3";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004DC";
	setAttr -s 65 ".wl";
	setAttr ".wl[0:64].w"
		2 0 0.85303043477234552 1 0.1469695652276545
		2 0 0.85303038347402782 1 0.14696961652597224
		2 0 0.67714297232902221 1 0.32285702767097785
		2 0 0.1831778249563954 1 0.81682217504360466
		2 0 0.1831778792925125 1 0.8168221207074875
		2 0 0.35194066313978878 1 0.64805933686021122
		2 1 0.23577069614708565 2 0.76422930385291432
		2 1 0.23577074919260113 2 0.7642292508073989
		2 1 0.38488283207408358 2 0.61511716792591653
		2 2 0.30762687632132579 3 0.69237312367867432
		2 2 0.30762692041074885 3 0.69237307958925109
		2 2 0.42116353835121845 3 0.57883646164878155
		2 3 0.39795289249161142 4 0.60204710750838852
		2 3 0.39795291806408561 4 0.60204708193591439
		2 3 0.459920349867457 4 0.540079650132543
		2 4 0.49999916149041412 5 0.50000083850958588
		2 4 0.49999916149063045 5 0.50000083850936949
		2 4 0.49999967567504555 5 0.50000032432495445
		2 5 0.60204553297957053 6 0.39795446702042947
		2 5 0.60204550740746543 6 0.39795449259253468
		2 5 0.54007901236353428 6 0.45992098763646583
		2 6 0.69237202830493227 7 0.30762797169506773
		2 6 0.69237198421569346 7 0.3076280157843066
		2 6 0.57883595618862316 7 0.42116404381137684
		2 7 0.76422863919583639 8 0.23577136080416372
		2 7 0.7642285861503697 8 0.23577141384963024
		2 7 0.61511679534367569 8 0.38488320465632425
		2 8 0.81682179355872186 10 0.18317820644127808
		2 8 0.81682173922259227 10 0.18317826077740773
		2 8 0.64805906600858254 10 0.35194093399141751
		2 9 0.5 10 0.5
		2 9 0.5 10 0.5
		2 9 0.5 10 0.5
		2 9 0.18317761954197762 11 0.81682238045802236
		2 9 0.18317767387808809 11 0.81682232612191197
		2 9 0.35194051729672693 11 0.64805948270327307
		2 11 0.23577052998317247 12 0.76422947001682751
		2 11 0.23577058302870027 12 0.76422941697129976
		2 11 0.38488273892858643 12 0.61511726107141362
		2 12 0.30762687632132873 13 0.69237312367867121
		2 12 0.30762692041075196 13 0.69237307958924799
		2 12 0.42116353835121995 13 0.57883646164878011
		2 13 0.39795315491286271 14 0.60204684508713724
		2 13 0.39795318048527512 14 0.60204681951472483
		2 13 0.45992045616226795 14 0.54007954383773205
		2 14 0.49999944099361204 15 0.50000055900638807
		2 14 0.49999944099375654 15 0.50000055900624352
		2 14 0.49999978378336485 15 0.50000021621663515
		2 15 0.6020455329795753 16 0.39795446702042464
		2 15 0.60204550740747009 16 0.39795449259252991
		2 15 0.54007901236353606 16 0.45992098763646394
		2 16 0.69237180922977826 17 0.30762819077022169
		2 16 0.6923717651405763 17 0.3076282348594237
		2 16 0.57883585509653956 17 0.42116414490346055
		2 17 0.76422830686645704 18 0.23577169313354301
		2 17 0.76422825382101522 18 0.2357717461789848
		2 17 0.61511660905241239 18 0.38488339094758767
		2 18 0.81682147076284595 19 0.18317852923715411
		2 18 0.81682141642670592 19 0.18317858357329411
		2 18 0.64805883682620558 19 0.35194116317379442
		2 18 0.14696956522765081 19 0.85303043477234919
		2 18 0.14696961652596841 19 0.85303038347403159
		2 18 0.32285702767097441 19 0.67714297232902565
		1 0 1
		1 19 1;
	setAttr -s 20 ".pm";
	setAttr ".pm[0]" -type "matrix" 0.99999999999999978 5.8958112037851259e-32 -1.2246467991473532e-16 0 2.2204460492503123e-16 1 -1.2246467991473532e-16 0
		 1.2246467991473532e-16 1.224646799147353e-16 1 0 1.9999999999999996 -6.1232338493354144e-18 -2.4492935982947064e-16 1;
	setAttr ".pm[1]" -type "matrix" 0.99999999999999978 5.8958112037851259e-32 -1.2246467991473532e-16 0 2.2204460492503123e-16 1 -1.2246467991473532e-16 0
		 1.2246467991473532e-16 1.224646799147353e-16 1 0 1.7777777776471888 -6.1232338493354205e-18 -1.6220383526783472e-16 1;
	setAttr ".pm[2]" -type "matrix" 0.99999999999999978 3.4306208749694645e-32 -1.2246467991473532e-16 0 2.2204460492503116e-16 0.99999999999999978 -1.224646799147353e-16 0
		 1.2246467991473532e-16 1.224646799147353e-16 1 0 1.5555555555288187 -6.123233849335476e-18 -1.7662282538961067e-16 1;
	setAttr ".pm[3]" -type "matrix" 0.99999999999999978 3.4306208749694645e-32 1.2246467991473532e-16 0 2.2204460492503116e-16 0.99999999999999978 1.224646799147353e-16 0
		 -1.2246467991473532e-16 -1.224646799147353e-16 1 0 1.3333333333309909 -6.123233849335503e-18 3.020641179641715e-16 1;
	setAttr ".pm[4]" -type "matrix" 0.99999999999999978 3.4306208749694645e-32 1.2246467991473532e-16 0 2.2204460492503116e-16 0.99999999999999978 1.224646799147353e-16 0
		 -1.2246467991473532e-16 -1.224646799147353e-16 1 0 1.1111111111115148 -6.1232338493355137e-18 2.7484974465012221e-16 1;
	setAttr ".pm[5]" -type "matrix" 0.99999999999999978 3.4306208749694645e-32 -1.2246467991473532e-16 0 2.2204460492503116e-16 0.99999999999999978 -1.224646799147353e-16 0
		 1.2246467991473532e-16 1.224646799147353e-16 1 0 0.88888888888848849 -6.1232338493354937e-18 -5.3346342026235679e-17 1;
	setAttr ".pm[6]" -type "matrix" 0.99999999999999978 3.4306208749694645e-32 -1.2246467991473532e-16 0 2.2204460492503116e-16 0.99999999999999978 -1.224646799147353e-16 0
		 1.2246467991473532e-16 1.224646799147353e-16 1 0 0.66666666666901109 -6.1232338493355099e-18 -9.5520907751258466e-17 1;
	setAttr ".pm[7]" -type "matrix" 0.99999999999999978 3.4306208749694645e-32 1.2246467991473532e-16 0 2.2204460492503116e-16 0.99999999999999978 1.224646799147353e-16 0
		 -1.2246467991473532e-16 -1.224646799147353e-16 1 0 0.44444444447118298 -6.1232338493355268e-18 1.3769547347893255e-16 1;
	setAttr ".pm[8]" -type "matrix" 0.99999999999999978 5.8958112037851259e-32 1.2246467991473532e-16 0 2.2204460492503123e-16 1 1.2246467991473532e-16 0
		 -1.2246467991473532e-16 -1.224646799147353e-16 1 0 0.22222222235281358 -6.1232338493355553e-18 1.2435888798507966e-16 1;
	setAttr ".pm[9]" -type "matrix" 0.99999999999999978 3.4306208749694645e-32 1.2246467991473532e-16 0 2.2204460492503116e-16 0.99999999999999978 1.224646799147353e-16 0
		 -1.2246467991473532e-16 -1.224646799147353e-16 1 0 1.6543612223867927e-24 -6.1232338493355322e-18 -7.4987967080113088e-34 1;
	setAttr ".pm[10]" -type "matrix" 0.99999999999999978 3.4306208749694645e-32 -1.2246467991473532e-16 0 2.2204460492503116e-16 0.99999999999999978 -1.224646799147353e-16 0
		 1.2246467991473532e-16 1.224646799147353e-16 1 0 2.0976023332915118e-16 -6.1232338493355315e-18 -2.2397621779311549e-32 1;
	setAttr ".pm[11]" -type "matrix" 0.99999999999999978 3.4306208749694645e-32 -1.2246467991473532e-16 0 2.2204460492503116e-16 0.99999999999999978 -1.224646799147353e-16 0
		 1.2246467991473532e-16 1.224646799147353e-16 1 0 -0.22222222235281164 -6.1232338493355322e-18 8.2725524561636054e-17 1;
	setAttr ".pm[12]" -type "matrix" 0.99999999999999978 3.4306208749694645e-32 -1.2246467991473532e-16 0 2.2204460492503116e-16 0.99999999999999978 -1.224646799147353e-16 0
		 1.2246467991473532e-16 1.224646799147353e-16 1 0 -0.44444444447118181 -6.1232338493355446e-18 6.8306534439860121e-17 1;
	setAttr ".pm[13]" -type "matrix" 0.99999999999999978 5.8958112037851259e-32 1.2246467991473532e-16 0 2.2204460492503123e-16 1 1.2246467991473532e-16 0
		 -1.2246467991473532e-16 -1.224646799147353e-16 1 0 -0.6666666666690092 -6.1232338493355885e-18 5.7134758134700792e-17 1;
	setAttr ".pm[14]" -type "matrix" 0.99999999999999978 5.8958112037851259e-32 1.2246467991473532e-16 0 2.2204460492503123e-16 1 1.2246467991473532e-16 0
		 -1.2246467991473532e-16 -1.224646799147353e-16 1 0 -0.88888888888848538 -6.1232338493356046e-18 2.992038482065145e-17 1;
	setAttr ".pm[15]" -type "matrix" 0.99999999999999978 3.4306208749694645e-32 -1.2246467991473532e-16 0 2.2204460492503116e-16 0.99999999999999978 -1.224646799147353e-16 0
		 1.2246467991473532e-16 1.224646799147353e-16 1 0 -1.1111111111115126 -6.1232338493355623e-18 1.9158301780323515e-16 1;
	setAttr ".pm[16]" -type "matrix" 0.99999999999999978 5.8958112037851259e-32 -1.2246467991473532e-16 0 2.2204460492503123e-16 1 -1.2246467991473532e-16 0
		 1.2246467991473532e-16 1.224646799147353e-16 1 0 -1.3333333333309889 -6.1232338493356123e-18 1.4940845207821222e-16 1;
	setAttr ".pm[17]" -type "matrix" 0.99999999999999978 3.4306208749694645e-32 1.2246467991473532e-16 0 2.2204460492503116e-16 0.99999999999999978 1.224646799147353e-16 0
		 -1.2246467991473532e-16 -1.224646799147353e-16 1 0 -1.5555555555288176 -6.1232338493355954e-18 -1.0723388635053821e-16 1;
	setAttr ".pm[18]" -type "matrix" 0.99999999999999978 3.4306208749694645e-32 1.2246467991473532e-16 0 2.2204460492503116e-16 0.99999999999999978 1.224646799147353e-16 0
		 -1.2246467991473532e-16 -1.224646799147353e-16 1 0 -1.7777777776471861 -6.1232338493356285e-18 -1.2057047184439101e-16 1;
	setAttr ".pm[19]" -type "matrix" 0.99999999999999978 3.4306208749694645e-32 1.2246467991473532e-16 0 2.2204460492503116e-16 0.99999999999999978 1.224646799147353e-16 0
		 -1.2246467991473532e-16 -1.224646799147353e-16 1 0 -1.9999999999999996 -6.1232338493356008e-18 -2.4492935982947064e-16 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 0 0 0 1;
	setAttr -s 20 ".ma";
	setAttr -s 20 ".dpf[0:19]"  4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4;
	setAttr -s 20 ".lw";
	setAttr -s 20 ".lw";
	setAttr ".mmi" yes;
	setAttr ".ucm" yes;
	setAttr -s 20 ".ifcl";
	setAttr -s 20 ".ifcl";
createNode tweak -n "tweak6";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004DD";
createNode objectSet -n "skinCluster3Set";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004DE";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster3GroupId";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004DF";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster3GroupParts";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004E0";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode objectSet -n "tweakSet6";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004E1";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId27";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004E2";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts24";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004E3";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode dagPose -n "bindPose3";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004E4";
	setAttr -s 43 ".wm";
	setAttr ".wm[0]" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 0 0 0 1;
	setAttr ".wm[1]" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 -1 0 0 1;
	setAttr ".wm[2]" -type "matrix" 2.2204460492503128e-16 0.99999999999999989 0 0 1 -2.2204460492503131e-16 1.2246467991473532e-16 0
		 1.2246467991473532e-16 -2.4651903288156619e-32 -1 0 -1.9999999999999998 0 0 1;
	setAttr ".wm[4]" -type "matrix" 2.2204460492503128e-16 0.99999999999999989 0 0 1 -2.2204460492503131e-16 1.2246467991473532e-16 0
		 1.2246467991473532e-16 -2.4651903288156619e-32 -1 0 -1.7777777759915034 0 0 1;
	setAttr ".wm[6]" -type "matrix" 2.2204460492503131e-16 1 0 0 1 -2.2204460492503131e-16 1.2246467991473532e-16 0
		 1.2246467991473532e-16 -2.4651903288156619e-32 -1 0 -1.5555555522174493 0 0 1;
	setAttr ".wm[8]" -type "matrix" 2.2204460492503131e-16 1 0 0 1 -2.2204460492503131e-16 -1.2246467991473532e-16 0
		 -1.2246467991473532e-16 2.4651903288156619e-32 -1 0 -1.3333333134627758 0 0 1;
	setAttr ".wm[10]" -type "matrix" 2.2204460492503131e-16 1 0 0 1 -2.2204460492503131e-16 -1.2246467991473532e-16 0
		 -1.2246467991473532e-16 2.4651903288156619e-32 -1 0 -1.111111104488776 0 0 1;
	setAttr ".wm[12]" -type "matrix" 2.2204460492503131e-16 1 0 0 1 -2.2204460492503131e-16 1.2246467991473532e-16 0
		 1.2246467991473532e-16 -2.4651903288156619e-32 -1 0 -0.88888883590658119 0 0 1;
	setAttr ".wm[14]" -type "matrix" 2.2204460492503131e-16 1 0 0 1 -2.2204460492503131e-16 1.2246467991473532e-16 0
		 1.2246467991473532e-16 -2.4651903288156619e-32 -1 0 -0.66666662693258016 0 0 1;
	setAttr ".wm[16]" -type "matrix" 2.2204460492503131e-16 1 0 0 1 -2.2204460492503131e-16 -1.2246467991473532e-16 0
		 -1.2246467991473532e-16 2.4651903288156619e-32 -1 0 -0.44444441798022899 0 0 1;
	setAttr ".wm[18]" -type "matrix" 2.2204460492503128e-16 0.99999999999999989 0 0 1 -2.2204460492503131e-16 -1.2246467991473532e-16 0
		 -1.2246467991473532e-16 2.4651903288156619e-32 -1 0 -0.22222220910733592 0 0 1;
	setAttr ".wm[20]" -type "matrix" 2.2204460492503131e-16 1 0 0 1 -2.2204460492503131e-16 -1.2246467991473532e-16 0
		 -1.2246467991473532e-16 2.4651903288156619e-32 -1 0 -1.6543612251060553e-24 0 0 1;
	setAttr ".wm[22]" -type "matrix" 1 0 0 0 0 1 0 0
		 0 0 1 0 1 0 0 1;
	setAttr ".wm[23]" -type "matrix" 2.2204460492503131e-16 1 0 0 1 -2.2204460492503131e-16 1.2246467991473532e-16 0
		 1.2246467991473532e-16 -2.4651903288156619e-32 -1 0 1.2284371595880083e-17 0 0 1;
	setAttr ".wm[25]" -type "matrix" 2.2204460492503131e-16 1 0 0 1 -2.2204460492503131e-16 1.2246467991473532e-16 0
		 1.2246467991473532e-16 -2.4651903288156619e-32 -1 0 0.22222222400849739 0 0 1;
	setAttr ".wm[27]" -type "matrix" 2.2204460492503131e-16 1 0 0 1 -2.2204460492503131e-16 1.2246467991473532e-16 0
		 1.2246467991473532e-16 -2.4651903288156619e-32 -1 0 0.44444444778255143 0 0 1;
	setAttr ".wm[29]" -type "matrix" 2.2204460492503128e-16 0.99999999999999989 0 0 1 -2.2204460492503131e-16 -1.2246467991473532e-16 0
		 -1.2246467991473532e-16 2.4651903288156619e-32 -1 0 0.66666668653722472 0 0 1;
	setAttr ".wm[31]" -type "matrix" 2.2204460492503128e-16 0.99999999999999989 0 0 1 -2.2204460492503131e-16 -1.2246467991473532e-16 0
		 -1.2246467991473532e-16 2.4651903288156619e-32 -1 0 0.88888889551122474 0 0 1;
	setAttr ".wm[33]" -type "matrix" 2.2204460492503131e-16 1 0 0 1 -2.2204460492503131e-16 1.2246467991473532e-16 0
		 1.2246467991473532e-16 -2.4651903288156619e-32 -1 0 1.1111111640934204 0 0 1;
	setAttr ".wm[35]" -type "matrix" 2.2204460492503128e-16 0.99999999999999989 0 0 1 -2.2204460492503131e-16 1.2246467991473532e-16 0
		 1.2246467991473532e-16 -2.4651903288156619e-32 -1 0 1.3333333730674204 0 0 1;
	setAttr ".wm[37]" -type "matrix" 2.2204460492503131e-16 1 0 0 1 -2.2204460492503131e-16 -1.2246467991473532e-16 0
		 -1.2246467991473532e-16 2.4651903288156619e-32 -1 0 1.555555582019772 0 0 1;
	setAttr ".wm[39]" -type "matrix" 2.2204460492503131e-16 1 0 0 1 -2.2204460492503131e-16 -1.2246467991473532e-16 0
		 -1.2246467991473532e-16 2.4651903288156619e-32 -1 0 1.7777777908926644 0 0 1;
	setAttr ".wm[41]" -type "matrix" 2.2204460492503131e-16 1 0 0 1 -2.2204460492503131e-16 -1.2246467991473532e-16 0
		 -1.2246467991473532e-16 2.4651903288156619e-32 -1 0 2 0 0 1;
	setAttr -s 43 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 -1
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[2]" -type "matrix" "xform" 0.99999999999999989 1 1 3.1415926535897931 -6.1232337580922408e-17 1.5707963267948966 0 -1.9999999999999998
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[3]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.1232338493354837e-18
		 -2.2204460492503131e-16 -2.4651903288156619e-32 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 -0.70710678118654768 -0.70710678118654746 4.3297802811774658e-17 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[4]" -type "matrix" "xform" 0.99999999999999989 1 1 3.1415926535897931 -6.1232337580922421e-17 1.5707963267948966 0 -1.7777777759915034
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[5]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.1232334816994559e-18
		 -1.65568569965302e-09 5.5511151028494813e-17 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 -0.70710678118654768 -0.70710678118654746 4.3297802811774658e-17 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[6]" -type "matrix" "xform" 1 1 1 3.1415926535897931 -6.1232337580922408e-17 1.5707963267948966 0 -1.5555555522174493
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[7]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.123233114063798e-18
		 -3.3113695119268982e-09 1.3877787402288651e-17 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 -0.70710678118654768 -0.70710678118654746 4.3297802811774658e-17 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[8]" -type "matrix" "xform" 1 1 1 -3.1415926535897931 -6.1232337580922408e-17 1.5707963267948966 0 -1.3333333134627758
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[9]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.1232294377054802e-18
		 -1.9868215461738004e-08 1.3877788051129921e-16 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0.70710678118654768 0.70710678118654746 4.3297802811774658e-17 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[10]" -type "matrix" "xform" 1 1 1 -3.1415926535897931 -6.123233758092231e-17 1.5707963267948966 0 -1.111111104488776
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[11]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.1232323787920475e-18
		 -6.6227391071205233e-09 1.387778788891962e-16 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0.70710678118654768 0.70710678118654746 4.3297802811774658e-17 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[12]" -type "matrix" "xform" 1 1 1 3.1415926535897931 -6.1232337580922347e-17 1.5707963267948966 0 -0.88888883590658119
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[13]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.1232220849888078e-18
		 -5.2981907527893668e-08 5.5511144742845475e-17 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 -0.70710678118654768 -0.70710678118654746 4.3297802811774658e-17 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[14]" -type "matrix" "xform" 1 1 1 3.1415926535897931 -6.1232337580922396e-17 1.5707963267948966 0 -0.66666662693258016
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[15]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.1232250260753658e-18
		 -3.9736431201031763e-08 -1.3877792674123782e-17 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 -0.70710678118654768 -0.70710678118654746 4.3297802811774658e-17 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[16]" -type "matrix" "xform" 1 1 1 -3.1415926535897931 -6.1232337580922384e-17 1.5707963267948966 0 -0.44444441798022899
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[17]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.1232279671620964e-18
		 -2.6490954097013741e-08 8.3266730091092953e-17 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0.70710678118654768 0.70710678118654746 4.3297802811774658e-17 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[18]" -type "matrix" "xform" 0.99999999999999989 1 1 -3.1415926535897931 -6.1232337580922371e-17 1.5707963267948966 0 -0.22222220910733592
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[19]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.1232309082486915e-18
		 -1.3245477714640685e-08 9.7144516276804384e-17 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0.70710678118654768 0.70710678118654746 4.3297802811774658e-17 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[20]" -type "matrix" "xform" 1 1 1 -3.1415926535897931 -6.1232337580922396e-17 1.5707963267948966 0 -1.6543612251060553e-24
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[21]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.1232338493355338e-18
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0.70710678118654768 0.70710678118654746 4.3297802811774658e-17 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[22]" -type "matrix" "xform" 1 1 1 0 0 0 0 1
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[23]" -type "matrix" "xform" 1 1 1 3.1415926535897931 -6.1232337580922396e-17 1.5707963267948966 0 1.2284371595880083e-17
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[24]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.1232338493354837e-18
		 -2.2204460492503131e-16 -2.4651903288156619e-32 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 -0.70710678118654768 -0.70710678118654746 4.3297802811774658e-17 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[25]" -type "matrix" "xform" 1 1 1 3.1415926535897931 -6.1232337580922384e-17 1.5707963267948966 0 0.22222222400849739
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[26]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.1232334816994559e-18
		 -1.65568569965302e-09 5.5511151028494813e-17 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 -0.70710678118654768 -0.70710678118654746 4.3297802811774658e-17 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[27]" -type "matrix" "xform" 1 1 1 3.1415926535897931 -6.1232337580922408e-17 1.5707963267948966 0 0.44444444778255143
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[28]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.123233114063798e-18
		 -3.3113695119268982e-09 1.3877787402288651e-17 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 -0.70710678118654768 -0.70710678118654746 4.3297802811774658e-17 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[29]" -type "matrix" "xform" 0.99999999999999989 1 1 -3.1415926535897931 -6.1232337580922359e-17 1.5707963267948966 0 0.66666668653722472
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[30]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.1232294377054802e-18
		 -1.9868215461738004e-08 1.3877788051129921e-16 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0.70710678118654768 0.70710678118654746 4.3297802811774658e-17 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[31]" -type "matrix" "xform" 0.99999999999999989 1 1 -3.1415926535897931 -6.1232337580922396e-17 1.5707963267948966 0 0.88888889551122474
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[32]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.1232323787920475e-18
		 -6.6227391071205233e-09 1.387778788891962e-16 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0.70710678118654768 0.70710678118654746 4.3297802811774658e-17 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[33]" -type "matrix" "xform" 1 1 1 3.1415926535897931 -6.1232337580922384e-17 1.5707963267948966 0 1.1111111640934204
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[34]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.1232220849888078e-18
		 -5.2981907527893668e-08 5.5511144742845475e-17 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 -0.70710678118654768 -0.70710678118654746 4.3297802811774658e-17 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[35]" -type "matrix" "xform" 0.99999999999999989 1 1 3.1415926535897931 -6.1232337580922347e-17 1.5707963267948966 0 1.3333333730674204
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[36]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.1232250260753658e-18
		 -3.9736431201031763e-08 -1.3877792674123782e-17 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 -0.70710678118654768 -0.70710678118654746 4.3297802811774658e-17 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[37]" -type "matrix" "xform" 1 1 1 -3.1415926535897931 -6.1232337580922384e-17 1.5707963267948966 0 1.555555582019772
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[38]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.1232279671620964e-18
		 -2.6490954097013741e-08 8.3266730091092953e-17 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0.70710678118654768 0.70710678118654746 4.3297802811774658e-17 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[39]" -type "matrix" "xform" 1 1 1 -3.1415926535897931 -6.1232337580922408e-17 1.5707963267948966 0 1.7777777908926644
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[40]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.1232309082486915e-18
		 -1.3245477714640685e-08 9.7144516276804384e-17 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0.70710678118654768 0.70710678118654746 4.3297802811774658e-17 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr ".xm[41]" -type "matrix" "xform" 1 1 1 -3.1415926535897931 -6.1232337580922396e-17 1.5707963267948966 0 2
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0 0 0 1 1
		 1 1 yes;
	setAttr ".xm[42]" -type "matrix" "xform" 1 1 1 0 0 0 0 6.1232338493355338e-18
		 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 1 0.70710678118654768 0.70710678118654746 4.3297802811774658e-17 4.3297802811774677e-17 1
		 1 1 yes;
	setAttr -s 43 ".m";
	setAttr -s 43 ".p";
	setAttr -s 43 ".g[0:42]" yes yes yes no yes no yes no yes no yes no 
		yes no yes no yes no yes no yes no yes yes no yes no yes no yes no yes no yes no 
		yes no yes no yes no yes no;
	setAttr ".bp" yes;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo1";
	rename -uid "7A4DA740-0000-0007-5F43-61A1000004E5";
	setAttr ".def" no;
	setAttr -s 6 ".tgi";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -3284.0658035688839 -221.42856262979359 ;
	setAttr ".tgi[0].vh" -type "double2" 1155.4944595792813 980.95234197283457 ;
	setAttr -s 148 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 1142.857177734375;
	setAttr ".tgi[0].ni[0].y" 771.4285888671875;
	setAttr ".tgi[0].ni[0].nvs" 18304;
	setAttr ".tgi[0].ni[1].x" 221.42857360839844;
	setAttr ".tgi[0].ni[1].y" 2114.28564453125;
	setAttr ".tgi[0].ni[1].nvs" 18304;
	setAttr ".tgi[0].ni[2].x" -1928.5714111328125;
	setAttr ".tgi[0].ni[2].y" 2124.28564453125;
	setAttr ".tgi[0].ni[2].nvs" 18304;
	setAttr ".tgi[0].ni[3].x" -368.57144165039062;
	setAttr ".tgi[0].ni[3].y" -18.571428298950195;
	setAttr ".tgi[0].ni[3].nvs" 18304;
	setAttr ".tgi[0].ni[4].x" -982.85711669921875;
	setAttr ".tgi[0].ni[4].y" -370;
	setAttr ".tgi[0].ni[4].nvs" 18304;
	setAttr ".tgi[0].ni[5].x" -3771.428466796875;
	setAttr ".tgi[0].ni[5].y" 2144.28564453125;
	setAttr ".tgi[0].ni[5].nvs" 18304;
	setAttr ".tgi[0].ni[6].x" 1450;
	setAttr ".tgi[0].ni[6].y" 1451.4285888671875;
	setAttr ".tgi[0].ni[6].nvs" 18304;
	setAttr ".tgi[0].ni[7].x" -982.85711669921875;
	setAttr ".tgi[0].ni[7].y" 362.85714721679688;
	setAttr ".tgi[0].ni[7].nvs" 18304;
	setAttr ".tgi[0].ni[8].x" 1142.857177734375;
	setAttr ".tgi[0].ni[8].y" 1550;
	setAttr ".tgi[0].ni[8].nvs" 18304;
	setAttr ".tgi[0].ni[9].x" -1745.935302734375;
	setAttr ".tgi[0].ni[9].y" 834.5037841796875;
	setAttr ".tgi[0].ni[9].nvs" 18305;
	setAttr ".tgi[0].ni[10].x" -675.71429443359375;
	setAttr ".tgi[0].ni[10].y" -497.14285278320312;
	setAttr ".tgi[0].ni[10].nvs" 18304;
	setAttr ".tgi[0].ni[11].x" -982.85711669921875;
	setAttr ".tgi[0].ni[11].y" -721.4285888671875;
	setAttr ".tgi[0].ni[11].nvs" 18304;
	setAttr ".tgi[0].ni[12].x" -982.85711669921875;
	setAttr ".tgi[0].ni[12].y" 865.71429443359375;
	setAttr ".tgi[0].ni[12].nvs" 18304;
	setAttr ".tgi[0].ni[13].x" -368.57144165039062;
	setAttr ".tgi[0].ni[13].y" -194.28572082519531;
	setAttr ".tgi[0].ni[13].nvs" 18304;
	setAttr ".tgi[0].ni[14].x" 1450;
	setAttr ".tgi[0].ni[14].y" -627.14288330078125;
	setAttr ".tgi[0].ni[14].nvs" 18304;
	setAttr ".tgi[0].ni[15].x" 1450;
	setAttr ".tgi[0].ni[15].y" 1870;
	setAttr ".tgi[0].ni[15].nvs" 18304;
	setAttr ".tgi[0].ni[16].x" -3464.28564453125;
	setAttr ".tgi[0].ni[16].y" 2321.428466796875;
	setAttr ".tgi[0].ni[16].nvs" 18304;
	setAttr ".tgi[0].ni[17].x" -982.85711669921875;
	setAttr ".tgi[0].ni[17].y" -545.71429443359375;
	setAttr ".tgi[0].ni[17].nvs" 18304;
	setAttr ".tgi[0].ni[18].x" 245.71427917480469;
	setAttr ".tgi[0].ni[18].y" 887.14288330078125;
	setAttr ".tgi[0].ni[18].nvs" 18304;
	setAttr ".tgi[0].ni[19].x" -2542.857177734375;
	setAttr ".tgi[0].ni[19].y" 2197.142822265625;
	setAttr ".tgi[0].ni[19].nvs" 18304;
	setAttr ".tgi[0].ni[20].x" 1450;
	setAttr ".tgi[0].ni[20].y" -881.4285888671875;
	setAttr ".tgi[0].ni[20].nvs" 18304;
	setAttr ".tgi[0].ni[21].x" -61.428569793701172;
	setAttr ".tgi[0].ni[21].y" 540;
	setAttr ".tgi[0].ni[21].nvs" 18304;
	setAttr ".tgi[0].ni[22].x" -982.85711669921875;
	setAttr ".tgi[0].ni[22].y" -18.571428298950195;
	setAttr ".tgi[0].ni[22].nvs" 18304;
	setAttr ".tgi[0].ni[23].x" -368.57144165039062;
	setAttr ".tgi[0].ni[23].y" -370;
	setAttr ".tgi[0].ni[23].nvs" 18304;
	setAttr ".tgi[0].ni[24].x" -1007.1428833007812;
	setAttr ".tgi[0].ni[24].y" 2231.428466796875;
	setAttr ".tgi[0].ni[24].nvs" 18304;
	setAttr ".tgi[0].ni[25].x" -675.71429443359375;
	setAttr ".tgi[0].ni[25].y" 914.28570556640625;
	setAttr ".tgi[0].ni[25].nvs" 18304;
	setAttr ".tgi[0].ni[26].x" 528.5714111328125;
	setAttr ".tgi[0].ni[26].y" 2471.428466796875;
	setAttr ".tgi[0].ni[26].nvs" 18304;
	setAttr ".tgi[0].ni[27].x" 1142.857177734375;
	setAttr ".tgi[0].ni[27].y" 1451.4285888671875;
	setAttr ".tgi[0].ni[27].nvs" 18304;
	setAttr ".tgi[0].ni[28].x" -1621.4285888671875;
	setAttr ".tgi[0].ni[28].y" 2088.571533203125;
	setAttr ".tgi[0].ni[28].nvs" 18304;
	setAttr ".tgi[0].ni[29].x" 1450;
	setAttr ".tgi[0].ni[29].y" 135.71427917480469;
	setAttr ".tgi[0].ni[29].nvs" 18304;
	setAttr ".tgi[0].ni[30].x" 245.71427917480469;
	setAttr ".tgi[0].ni[30].y" -348.57144165039062;
	setAttr ".tgi[0].ni[30].nvs" 18304;
	setAttr ".tgi[0].ni[31].x" -675.71429443359375;
	setAttr ".tgi[0].ni[31].y" 688.5714111328125;
	setAttr ".tgi[0].ni[31].nvs" 18304;
	setAttr ".tgi[0].ni[32].x" -2235.71435546875;
	setAttr ".tgi[0].ni[32].y" 2227.142822265625;
	setAttr ".tgi[0].ni[32].nvs" 18304;
	setAttr ".tgi[0].ni[33].x" 835.71429443359375;
	setAttr ".tgi[0].ni[33].y" 1550;
	setAttr ".tgi[0].ni[33].nvs" 18304;
	setAttr ".tgi[0].ni[34].x" 528.5714111328125;
	setAttr ".tgi[0].ni[34].y" 2045.7142333984375;
	setAttr ".tgi[0].ni[34].nvs" 18304;
	setAttr ".tgi[0].ni[35].x" 245.71427917480469;
	setAttr ".tgi[0].ni[35].y" 738.5714111328125;
	setAttr ".tgi[0].ni[35].nvs" 18304;
	setAttr ".tgi[0].ni[36].x" 1450;
	setAttr ".tgi[0].ni[36].y" 262.85714721679688;
	setAttr ".tgi[0].ni[36].nvs" 18304;
	setAttr ".tgi[0].ni[37].x" 835.71429443359375;
	setAttr ".tgi[0].ni[37].y" 1254.2857666015625;
	setAttr ".tgi[0].ni[37].nvs" 18304;
	setAttr ".tgi[0].ni[38].x" 1450;
	setAttr ".tgi[0].ni[38].y" 1352.857177734375;
	setAttr ".tgi[0].ni[38].nvs" 18304;
	setAttr ".tgi[0].ni[39].x" -61.428569793701172;
	setAttr ".tgi[0].ni[39].y" 717.14288330078125;
	setAttr ".tgi[0].ni[39].nvs" 18304;
	setAttr ".tgi[0].ni[40].x" 245.71427917480469;
	setAttr ".tgi[0].ni[40].y" -700;
	setAttr ".tgi[0].ni[40].nvs" 18304;
	setAttr ".tgi[0].ni[41].x" 1142.857177734375;
	setAttr ".tgi[0].ni[41].y" 1705.7142333984375;
	setAttr ".tgi[0].ni[41].nvs" 18304;
	setAttr ".tgi[0].ni[42].x" -1621.4285888671875;
	setAttr ".tgi[0].ni[42].y" 2301.428466796875;
	setAttr ".tgi[0].ni[42].nvs" 18304;
	setAttr ".tgi[0].ni[43].x" 835.71429443359375;
	setAttr ".tgi[0].ni[43].y" 1705.7142333984375;
	setAttr ".tgi[0].ni[43].nvs" 18304;
	setAttr ".tgi[0].ni[44].x" 835.71429443359375;
	setAttr ".tgi[0].ni[44].y" 1451.4285888671875;
	setAttr ".tgi[0].ni[44].nvs" 18304;
	setAttr ".tgi[0].ni[45].x" -3157.142822265625;
	setAttr ".tgi[0].ni[45].y" 2247.142822265625;
	setAttr ".tgi[0].ni[45].nvs" 18304;
	setAttr ".tgi[0].ni[46].x" 835.71429443359375;
	setAttr ".tgi[0].ni[46].y" 1352.857177734375;
	setAttr ".tgi[0].ni[46].nvs" 18304;
	setAttr ".tgi[0].ni[47].x" 221.42857360839844;
	setAttr ".tgi[0].ni[47].y" 1818.5714111328125;
	setAttr ".tgi[0].ni[47].nvs" 18304;
	setAttr ".tgi[0].ni[48].x" -368.57144165039062;
	setAttr ".tgi[0].ni[48].y" -721.4285888671875;
	setAttr ".tgi[0].ni[48].nvs" 18304;
	setAttr ".tgi[0].ni[49].x" 1142.857177734375;
	setAttr ".tgi[0].ni[49].y" 1057.142822265625;
	setAttr ".tgi[0].ni[49].nvs" 18304;
	setAttr ".tgi[0].ni[50].x" 1450;
	setAttr ".tgi[0].ni[50].y" -372.85714721679688;
	setAttr ".tgi[0].ni[50].nvs" 18304;
	setAttr ".tgi[0].ni[51].x" 835.71429443359375;
	setAttr ".tgi[0].ni[51].y" 1870;
	setAttr ".tgi[0].ni[51].nvs" 18304;
	setAttr ".tgi[0].ni[52].x" 835.71429443359375;
	setAttr ".tgi[0].ni[52].y" 2422.857177734375;
	setAttr ".tgi[0].ni[52].nvs" 18304;
	setAttr ".tgi[0].ni[53].x" -3771.428466796875;
	setAttr ".tgi[0].ni[53].y" 2242.857177734375;
	setAttr ".tgi[0].ni[53].nvs" 18304;
	setAttr ".tgi[0].ni[54].x" 835.71429443359375;
	setAttr ".tgi[0].ni[54].y" 2074.28564453125;
	setAttr ".tgi[0].ni[54].nvs" 18304;
	setAttr ".tgi[0].ni[55].x" -85.714286804199219;
	setAttr ".tgi[0].ni[55].y" 1814.2857666015625;
	setAttr ".tgi[0].ni[55].nvs" 18304;
	setAttr ".tgi[0].ni[56].x" 1450;
	setAttr ".tgi[0].ni[56].y" 1705.7142333984375;
	setAttr ".tgi[0].ni[56].nvs" 18304;
	setAttr ".tgi[0].ni[57].x" 528.5714111328125;
	setAttr ".tgi[0].ni[57].y" 1422.857177734375;
	setAttr ".tgi[0].ni[57].nvs" 18304;
	setAttr ".tgi[0].ni[58].x" 1142.857177734375;
	setAttr ".tgi[0].ni[58].y" 1155.7142333984375;
	setAttr ".tgi[0].ni[58].nvs" 18304;
	setAttr ".tgi[0].ni[59].x" 1450;
	setAttr ".tgi[0].ni[59].y" -1390;
	setAttr ".tgi[0].ni[59].nvs" 18304;
	setAttr ".tgi[0].ni[60].x" 528.5714111328125;
	setAttr ".tgi[0].ni[60].y" 1054.2857666015625;
	setAttr ".tgi[0].ni[60].nvs" 18304;
	setAttr ".tgi[0].ni[61].x" 1450;
	setAttr ".tgi[0].ni[61].y" -500;
	setAttr ".tgi[0].ni[61].nvs" 18304;
	setAttr ".tgi[0].ni[62].x" 1450;
	setAttr ".tgi[0].ni[62].y" 8.5714282989501953;
	setAttr ".tgi[0].ni[62].nvs" 18304;
	setAttr ".tgi[0].ni[63].x" 1450;
	setAttr ".tgi[0].ni[63].y" 390;
	setAttr ".tgi[0].ni[63].nvs" 18304;
	setAttr ".tgi[0].ni[64].x" 528.5714111328125;
	setAttr ".tgi[0].ni[64].y" 898.5714111328125;
	setAttr ".tgi[0].ni[64].nvs" 18304;
	setAttr ".tgi[0].ni[65].x" -1314.2857666015625;
	setAttr ".tgi[0].ni[65].y" 2272.857177734375;
	setAttr ".tgi[0].ni[65].nvs" 18304;
	setAttr ".tgi[0].ni[66].x" -3771.428466796875;
	setAttr ".tgi[0].ni[66].y" 2341.428466796875;
	setAttr ".tgi[0].ni[66].nvs" 18304;
	setAttr ".tgi[0].ni[67].x" -2850;
	setAttr ".tgi[0].ni[67].y" 2172.857177734375;
	setAttr ".tgi[0].ni[67].nvs" 18304;
	setAttr ".tgi[0].ni[68].x" 1450;
	setAttr ".tgi[0].ni[68].y" -245.71427917480469;
	setAttr ".tgi[0].ni[68].nvs" 18304;
	setAttr ".tgi[0].ni[69].x" 528.5714111328125;
	setAttr ".tgi[0].ni[69].y" 1521.4285888671875;
	setAttr ".tgi[0].ni[69].nvs" 18304;
	setAttr ".tgi[0].ni[70].x" -368.57144165039062;
	setAttr ".tgi[0].ni[70].y" -545.71429443359375;
	setAttr ".tgi[0].ni[70].nvs" 18304;
	setAttr ".tgi[0].ni[71].x" -2235.71435546875;
	setAttr ".tgi[0].ni[71].y" 2014.2857666015625;
	setAttr ".tgi[0].ni[71].nvs" 18304;
	setAttr ".tgi[0].ni[72].x" 221.42857360839844;
	setAttr ".tgi[0].ni[72].y" 2270;
	setAttr ".tgi[0].ni[72].nvs" 18304;
	setAttr ".tgi[0].ni[73].x" -2850;
	setAttr ".tgi[0].ni[73].y" 2271.428466796875;
	setAttr ".tgi[0].ni[73].nvs" 18304;
	setAttr ".tgi[0].ni[74].x" -61.428569793701172;
	setAttr ".tgi[0].ni[74].y" -370;
	setAttr ".tgi[0].ni[74].nvs" 18304;
	setAttr ".tgi[0].ni[75].x" -675.71429443359375;
	setAttr ".tgi[0].ni[75].y" -145.71427917480469;
	setAttr ".tgi[0].ni[75].nvs" 18304;
	setAttr ".tgi[0].ni[76].x" -85.714286804199219;
	setAttr ".tgi[0].ni[76].y" 1912.857177734375;
	setAttr ".tgi[0].ni[76].nvs" 18304;
	setAttr ".tgi[0].ni[77].x" 221.42857360839844;
	setAttr ".tgi[0].ni[77].y" 1720;
	setAttr ".tgi[0].ni[77].nvs" 18304;
	setAttr ".tgi[0].ni[78].x" 835.71429443359375;
	setAttr ".tgi[0].ni[78].y" 2238.571533203125;
	setAttr ".tgi[0].ni[78].nvs" 18304;
	setAttr ".tgi[0].ni[79].x" 1142.857177734375;
	setAttr ".tgi[0].ni[79].y" 2074.28564453125;
	setAttr ".tgi[0].ni[79].nvs" 18304;
	setAttr ".tgi[0].ni[80].x" 1450;
	setAttr ".tgi[0].ni[80].y" -1644.2857666015625;
	setAttr ".tgi[0].ni[80].nvs" 18304;
	setAttr ".tgi[0].ni[81].x" -1687.142822265625;
	setAttr ".tgi[0].ni[81].y" 341.42855834960938;
	setAttr ".tgi[0].ni[81].nvs" 18304;
	setAttr ".tgi[0].ni[82].x" -368.57144165039062;
	setAttr ".tgi[0].ni[82].y" 865.71429443359375;
	setAttr ".tgi[0].ni[82].nvs" 18304;
	setAttr ".tgi[0].ni[83].x" 528.5714111328125;
	setAttr ".tgi[0].ni[83].y" 1947.142822265625;
	setAttr ".tgi[0].ni[83].nvs" 18304;
	setAttr ".tgi[0].ni[84].x" 1450;
	setAttr ".tgi[0].ni[84].y" -1262.857177734375;
	setAttr ".tgi[0].ni[84].nvs" 18304;
	setAttr ".tgi[0].ni[85].x" -61.428569793701172;
	setAttr ".tgi[0].ni[85].y" -545.71429443359375;
	setAttr ".tgi[0].ni[85].nvs" 18304;
	setAttr ".tgi[0].ni[86].x" -700;
	setAttr ".tgi[0].ni[86].y" 2137.142822265625;
	setAttr ".tgi[0].ni[86].nvs" 18304;
	setAttr ".tgi[0].ni[87].x" -3157.142822265625;
	setAttr ".tgi[0].ni[87].y" 2148.571533203125;
	setAttr ".tgi[0].ni[87].nvs" 18304;
	setAttr ".tgi[0].ni[88].x" 1450;
	setAttr ".tgi[0].ni[88].y" -118.57142639160156;
	setAttr ".tgi[0].ni[88].nvs" 18304;
	setAttr ".tgi[0].ni[89].x" 1142.857177734375;
	setAttr ".tgi[0].ni[89].y" 1352.857177734375;
	setAttr ".tgi[0].ni[89].nvs" 18304;
	setAttr ".tgi[0].ni[90].x" 1450;
	setAttr ".tgi[0].ni[90].y" 2238.571533203125;
	setAttr ".tgi[0].ni[90].nvs" 18304;
	setAttr ".tgi[0].ni[91].x" 1142.857177734375;
	setAttr ".tgi[0].ni[91].y" 1254.2857666015625;
	setAttr ".tgi[0].ni[91].nvs" 18304;
	setAttr ".tgi[0].ni[92].x" 245.71427917480469;
	setAttr ".tgi[0].ni[92].y" 2.8571429252624512;
	setAttr ".tgi[0].ni[92].nvs" 18304;
	setAttr ".tgi[0].ni[93].x" 528.5714111328125;
	setAttr ".tgi[0].ni[93].y" 1210;
	setAttr ".tgi[0].ni[93].nvs" 18304;
	setAttr ".tgi[0].ni[94].x" -368.57144165039062;
	setAttr ".tgi[0].ni[94].y" 540;
	setAttr ".tgi[0].ni[94].nvs" 18304;
	setAttr ".tgi[0].ni[95].x" -982.85711669921875;
	setAttr ".tgi[0].ni[95].y" 540;
	setAttr ".tgi[0].ni[95].nvs" 18304;
	setAttr ".tgi[0].ni[96].x" -368.57144165039062;
	setAttr ".tgi[0].ni[96].y" 717.14288330078125;
	setAttr ".tgi[0].ni[96].nvs" 18304;
	setAttr ".tgi[0].ni[97].x" 1450;
	setAttr ".tgi[0].ni[97].y" -754.28570556640625;
	setAttr ".tgi[0].ni[97].nvs" 18304;
	setAttr ".tgi[0].ni[98].x" 245.71427917480469;
	setAttr ".tgi[0].ni[98].y" -524.28570556640625;
	setAttr ".tgi[0].ni[98].nvs" 18304;
	setAttr ".tgi[0].ni[99].x" 1450;
	setAttr ".tgi[0].ni[99].y" 2074.28564453125;
	setAttr ".tgi[0].ni[99].nvs" 18304;
	setAttr ".tgi[0].ni[100].x" -1314.2857666015625;
	setAttr ".tgi[0].ni[100].y" 2174.28564453125;
	setAttr ".tgi[0].ni[100].nvs" 18304;
	setAttr ".tgi[0].ni[101].x" 1450;
	setAttr ".tgi[0].ni[101].y" 1550;
	setAttr ".tgi[0].ni[101].nvs" 18304;
	setAttr ".tgi[0].ni[102].x" -675.71429443359375;
	setAttr ".tgi[0].ni[102].y" 334.28570556640625;
	setAttr ".tgi[0].ni[102].nvs" 18304;
	setAttr ".tgi[0].ni[103].x" -368.57144165039062;
	setAttr ".tgi[0].ni[103].y" 362.85714721679688;
	setAttr ".tgi[0].ni[103].nvs" 18304;
	setAttr ".tgi[0].ni[104].x" 221.42857360839844;
	setAttr ".tgi[0].ni[104].y" 1917.142822265625;
	setAttr ".tgi[0].ni[104].nvs" 18304;
	setAttr ".tgi[0].ni[105].x" 221.42857360839844;
	setAttr ".tgi[0].ni[105].y" 2015.7142333984375;
	setAttr ".tgi[0].ni[105].nvs" 18304;
	setAttr ".tgi[0].ni[106].x" -982.85711669921875;
	setAttr ".tgi[0].ni[106].y" -194.28572082519531;
	setAttr ".tgi[0].ni[106].nvs" 18304;
	setAttr ".tgi[0].ni[107].x" 1142.857177734375;
	setAttr ".tgi[0].ni[107].y" 2238.571533203125;
	setAttr ".tgi[0].ni[107].nvs" 18304;
	setAttr ".tgi[0].ni[108].x" 528.5714111328125;
	setAttr ".tgi[0].ni[108].y" 2315.71435546875;
	setAttr ".tgi[0].ni[108].nvs" 18304;
	setAttr ".tgi[0].ni[109].x" 1450;
	setAttr ".tgi[0].ni[109].y" -1517.142822265625;
	setAttr ".tgi[0].ni[109].nvs" 18304;
	setAttr ".tgi[0].ni[110].x" 245.71427917480469;
	setAttr ".tgi[0].ni[110].y" 384.28570556640625;
	setAttr ".tgi[0].ni[110].nvs" 18304;
	setAttr ".tgi[0].ni[111].x" -675.71429443359375;
	setAttr ".tgi[0].ni[111].y" 511.42855834960938;
	setAttr ".tgi[0].ni[111].nvs" 18304;
	setAttr ".tgi[0].ni[112].x" -392.85714721679688;
	setAttr ".tgi[0].ni[112].y" 2000;
	setAttr ".tgi[0].ni[112].nvs" 18304;
	setAttr ".tgi[0].ni[113].x" -61.428569793701172;
	setAttr ".tgi[0].ni[113].y" 185.71427917480469;
	setAttr ".tgi[0].ni[113].nvs" 18304;
	setAttr ".tgi[0].ni[114].x" 835.71429443359375;
	setAttr ".tgi[0].ni[114].y" 1155.7142333984375;
	setAttr ".tgi[0].ni[114].nvs" 18304;
	setAttr ".tgi[0].ni[115].x" -675.71429443359375;
	setAttr ".tgi[0].ni[115].y" 30;
	setAttr ".tgi[0].ni[115].nvs" 18304;
	setAttr ".tgi[0].ni[116].x" 245.71427917480469;
	setAttr ".tgi[0].ni[116].y" 561.4285888671875;
	setAttr ".tgi[0].ni[116].nvs" 18304;
	setAttr ".tgi[0].ni[117].x" 221.42857360839844;
	setAttr ".tgi[0].ni[117].y" 1424.2857666015625;
	setAttr ".tgi[0].ni[117].nvs" 18304;
	setAttr ".tgi[0].ni[118].x" 1450;
	setAttr ".tgi[0].ni[118].y" 1254.2857666015625;
	setAttr ".tgi[0].ni[118].nvs" 18304;
	setAttr ".tgi[0].ni[119].x" -982.85711669921875;
	setAttr ".tgi[0].ni[119].y" 717.14288330078125;
	setAttr ".tgi[0].ni[119].nvs" 18304;
	setAttr ".tgi[0].ni[120].x" -1007.1428833007812;
	setAttr ".tgi[0].ni[120].y" 2132.857177734375;
	setAttr ".tgi[0].ni[120].nvs" 18304;
	setAttr ".tgi[0].ni[121].x" 1450;
	setAttr ".tgi[0].ni[121].y" 771.4285888671875;
	setAttr ".tgi[0].ni[121].nvs" 18304;
	setAttr ".tgi[0].ni[122].x" -61.428569793701172;
	setAttr ".tgi[0].ni[122].y" 865.71429443359375;
	setAttr ".tgi[0].ni[122].nvs" 18304;
	setAttr ".tgi[0].ni[123].x" 1450;
	setAttr ".tgi[0].ni[123].y" 1155.7142333984375;
	setAttr ".tgi[0].ni[123].nvs" 18304;
	setAttr ".tgi[0].ni[124].x" -2068.571533203125;
	setAttr ".tgi[0].ni[124].y" 412.85714721679688;
	setAttr ".tgi[0].ni[124].nvs" 18304;
	setAttr ".tgi[0].ni[125].x" -61.428569793701172;
	setAttr ".tgi[0].ni[125].y" -18.571428298950195;
	setAttr ".tgi[0].ni[125].nvs" 18304;
	setAttr ".tgi[0].ni[126].x" 1142.857177734375;
	setAttr ".tgi[0].ni[126].y" 1870;
	setAttr ".tgi[0].ni[126].nvs" 18304;
	setAttr ".tgi[0].ni[127].x" -1587.4840087890625;
	setAttr ".tgi[0].ni[127].y" -57.925437927246094;
	setAttr ".tgi[0].ni[127].nvs" 18304;
	setAttr ".tgi[0].ni[128].x" -675.71429443359375;
	setAttr ".tgi[0].ni[128].y" 157.14285278320312;
	setAttr ".tgi[0].ni[128].nvs" 18304;
	setAttr ".tgi[0].ni[129].x" 221.42857360839844;
	setAttr ".tgi[0].ni[129].y" 1522.857177734375;
	setAttr ".tgi[0].ni[129].nvs" 18304;
	setAttr ".tgi[0].ni[130].x" 528.5714111328125;
	setAttr ".tgi[0].ni[130].y" 1677.142822265625;
	setAttr ".tgi[0].ni[130].nvs" 18304;
	setAttr ".tgi[0].ni[131].x" 1142.857177734375;
	setAttr ".tgi[0].ni[131].y" 2422.857177734375;
	setAttr ".tgi[0].ni[131].nvs" 18304;
	setAttr ".tgi[0].ni[132].x" 221.42857360839844;
	setAttr ".tgi[0].ni[132].y" 1621.4285888671875;
	setAttr ".tgi[0].ni[132].nvs" 18304;
	setAttr ".tgi[0].ni[133].x" -675.71429443359375;
	setAttr ".tgi[0].ni[133].y" -321.42855834960938;
	setAttr ".tgi[0].ni[133].nvs" 18304;
	setAttr ".tgi[0].ni[134].x" 221.42857360839844;
	setAttr ".tgi[0].ni[134].y" 1325.7142333984375;
	setAttr ".tgi[0].ni[134].nvs" 18304;
	setAttr ".tgi[0].ni[135].x" -61.428569793701172;
	setAttr ".tgi[0].ni[135].y" -721.4285888671875;
	setAttr ".tgi[0].ni[135].nvs" 18304;
	setAttr ".tgi[0].ni[136].x" -675.71429443359375;
	setAttr ".tgi[0].ni[136].y" -672.85711669921875;
	setAttr ".tgi[0].ni[136].nvs" 18304;
	setAttr ".tgi[0].ni[137].x" 1450;
	setAttr ".tgi[0].ni[137].y" 517.14288330078125;
	setAttr ".tgi[0].ni[137].nvs" 18304;
	setAttr ".tgi[0].ni[138].x" -61.428569793701172;
	setAttr ".tgi[0].ni[138].y" 362.85714721679688;
	setAttr ".tgi[0].ni[138].nvs" 18304;
	setAttr ".tgi[0].ni[139].x" 245.71427917480469;
	setAttr ".tgi[0].ni[139].y" -172.85714721679688;
	setAttr ".tgi[0].ni[139].nvs" 18304;
	setAttr ".tgi[0].ni[140].x" -3464.28564453125;
	setAttr ".tgi[0].ni[140].y" 2420;
	setAttr ".tgi[0].ni[140].nvs" 18304;
	setAttr ".tgi[0].ni[141].x" 245.71427917480469;
	setAttr ".tgi[0].ni[141].y" 207.14285278320312;
	setAttr ".tgi[0].ni[141].nvs" 18304;
	setAttr ".tgi[0].ni[142].x" -982.85711669921875;
	setAttr ".tgi[0].ni[142].y" 185.71427917480469;
	setAttr ".tgi[0].ni[142].nvs" 18304;
	setAttr ".tgi[0].ni[143].x" 1450;
	setAttr ".tgi[0].ni[143].y" 2422.857177734375;
	setAttr ".tgi[0].ni[143].nvs" 18304;
	setAttr ".tgi[0].ni[144].x" 1450;
	setAttr ".tgi[0].ni[144].y" 644.28570556640625;
	setAttr ".tgi[0].ni[144].nvs" 18304;
	setAttr ".tgi[0].ni[145].x" -61.428569793701172;
	setAttr ".tgi[0].ni[145].y" -194.28572082519531;
	setAttr ".tgi[0].ni[145].nvs" 18304;
	setAttr ".tgi[0].ni[146].x" -368.57144165039062;
	setAttr ".tgi[0].ni[146].y" 185.71427917480469;
	setAttr ".tgi[0].ni[146].nvs" 18304;
	setAttr ".tgi[0].ni[147].x" 1142.857177734375;
	setAttr ".tgi[0].ni[147].y" 958.5714111328125;
	setAttr ".tgi[0].ni[147].nvs" 18304;
	setAttr ".tgi[1].tn" -type "string" "Untitled_2";
	setAttr ".tgi[1].vl" -type "double2" 2542.5365290053055 4083.3331710762313 ;
	setAttr ".tgi[1].vh" -type "double2" 6977.7011879325328 5284.5235995356888 ;
	setAttr ".tgi[1].ni[0].x" 4445.71435546875;
	setAttr ".tgi[1].ni[0].y" 4805.71435546875;
	setAttr ".tgi[1].ni[0].nvs" 18305;
	setAttr ".tgi[2].tn" -type "string" "Untitled_3";
	setAttr ".tgi[2].vl" -type "double2" 542.03294549451266 2154.7618191393631 ;
	setAttr ".tgi[2].vh" -type "double2" 2950.8240585689628 2807.1427455970265 ;
	setAttr -s 22 ".tgi[2].ni";
	setAttr ".tgi[2].ni[0].x" 1548.5714111328125;
	setAttr ".tgi[2].ni[0].y" 2275.71435546875;
	setAttr ".tgi[2].ni[0].nvs" 18304;
	setAttr ".tgi[2].ni[1].x" 1954.2857666015625;
	setAttr ".tgi[2].ni[1].y" 2270;
	setAttr ".tgi[2].ni[1].nvs" 18304;
	setAttr ".tgi[2].ni[2].x" 1181.4285888671875;
	setAttr ".tgi[2].ni[2].y" 2540;
	setAttr ".tgi[2].ni[2].nvs" 18304;
	setAttr ".tgi[2].ni[3].x" 1810;
	setAttr ".tgi[2].ni[3].y" 2374.28564453125;
	setAttr ".tgi[2].ni[3].nvs" 18304;
	setAttr ".tgi[2].ni[4].x" 1502.857177734375;
	setAttr ".tgi[2].ni[4].y" 2374.28564453125;
	setAttr ".tgi[2].ni[4].nvs" 18304;
	setAttr ".tgi[2].ni[5].x" 2117.142822265625;
	setAttr ".tgi[2].ni[5].y" 2572.857177734375;
	setAttr ".tgi[2].ni[5].nvs" 18304;
	setAttr ".tgi[2].ni[6].x" 2117.142822265625;
	setAttr ".tgi[2].ni[6].y" 2374.28564453125;
	setAttr ".tgi[2].ni[6].nvs" 18304;
	setAttr ".tgi[2].ni[7].x" 1140.8721923828125;
	setAttr ".tgi[2].ni[7].y" 2592.810791015625;
	setAttr ".tgi[2].ni[7].nvs" 18305;
	setAttr ".tgi[2].ni[8].x" 1645.9803466796875;
	setAttr ".tgi[2].ni[8].y" 2398.05126953125;
	setAttr ".tgi[2].ni[8].nvs" 18304;
	setAttr ".tgi[2].ni[9].x" 1650.5909423828125;
	setAttr ".tgi[2].ni[9].y" 2633.325927734375;
	setAttr ".tgi[2].ni[9].nvs" 18304;
	setAttr ".tgi[2].ni[10].x" 1954.2857666015625;
	setAttr ".tgi[2].ni[10].y" 2397.142822265625;
	setAttr ".tgi[2].ni[10].nvs" 18304;
	setAttr ".tgi[2].ni[11].x" 2002.55908203125;
	setAttr ".tgi[2].ni[11].y" 2572.55908203125;
	setAttr ".tgi[2].ni[11].nvs" 18305;
	setAttr ".tgi[2].ni[12].x" 1802.857177734375;
	setAttr ".tgi[2].ni[12].y" 2452.857177734375;
	setAttr ".tgi[2].ni[12].nvs" 18304;
	setAttr ".tgi[2].ni[13].x" 1502.857177734375;
	setAttr ".tgi[2].ni[13].y" 2657.142822265625;
	setAttr ".tgi[2].ni[13].nvs" 18304;
	setAttr ".tgi[2].ni[14].x" 1647.142822265625;
	setAttr ".tgi[2].ni[14].y" 2525.147705078125;
	setAttr ".tgi[2].ni[14].nvs" 18304;
	setAttr ".tgi[2].ni[15].x" 1502.857177734375;
	setAttr ".tgi[2].ni[15].y" 2501.428466796875;
	setAttr ".tgi[2].ni[15].nvs" 18304;
	setAttr ".tgi[2].ni[16].x" 1981.008544921875;
	setAttr ".tgi[2].ni[16].y" 2771.252685546875;
	setAttr ".tgi[2].ni[16].nvs" 18305;
	setAttr ".tgi[2].ni[17].x" 1195.7142333984375;
	setAttr ".tgi[2].ni[17].y" 2534.28564453125;
	setAttr ".tgi[2].ni[17].nvs" 18304;
	setAttr ".tgi[2].ni[18].x" 1810;
	setAttr ".tgi[2].ni[18].y" 2555.71435546875;
	setAttr ".tgi[2].ni[18].nvs" 18304;
	setAttr ".tgi[2].ni[19].x" 1340;
	setAttr ".tgi[2].ni[19].y" 2750;
	setAttr ".tgi[2].ni[19].nvs" 18304;
	setAttr ".tgi[2].ni[20].x" 1647.142822265625;
	setAttr ".tgi[2].ni[20].y" 2750;
	setAttr ".tgi[2].ni[20].nvs" 18304;
	setAttr ".tgi[2].ni[21].x" 1340;
	setAttr ".tgi[2].ni[21].y" 2524.28564453125;
	setAttr ".tgi[2].ni[21].nvs" 18304;
	setAttr ".tgi[3].tn" -type "string" "Untitled_4";
	setAttr ".tgi[3].vl" -type "double2" 3606.9595636320123 -7802.3806423422011 ;
	setAttr ".tgi[3].vh" -type "double2" 6745.4209773822986 -6952.3806761181659 ;
	setAttr ".tgi[4].tn" -type "string" "Untitled_5";
	setAttr ".tgi[4].vl" -type "double2" 2922.0694809569745 -12659.523306479603 ;
	setAttr ".tgi[4].vh" -type "double2" 5937.4539765209756 -11842.856672264355 ;
	setAttr ".tgi[5].tn" -type "string" "Untitled_6";
	setAttr ".tgi[5].vl" -type "double2" -1082.0970265983974 491.66664712958959 ;
	setAttr ".tgi[5].vh" -type "double2" 2504.716017687645 1463.0951799570591 ;
	setAttr -s 35 ".tgi[5].ni";
	setAttr ".tgi[5].ni[0].x" 2941.428466796875;
	setAttr ".tgi[5].ni[0].y" 1058.5714111328125;
	setAttr ".tgi[5].ni[0].nvs" 18304;
	setAttr ".tgi[5].ni[1].x" 1712.857177734375;
	setAttr ".tgi[5].ni[1].y" 1078.5714111328125;
	setAttr ".tgi[5].ni[1].nvs" 18304;
	setAttr ".tgi[5].ni[2].x" 2650;
	setAttr ".tgi[5].ni[2].y" 407.14285278320312;
	setAttr ".tgi[5].ni[2].nvs" 18304;
	setAttr ".tgi[5].ni[3].x" 484.28570556640625;
	setAttr ".tgi[5].ni[3].y" 1002.8571166992188;
	setAttr ".tgi[5].ni[3].nvs" 18304;
	setAttr ".tgi[5].ni[4].x" 177.14285278320312;
	setAttr ".tgi[5].ni[4].y" 1062.857177734375;
	setAttr ".tgi[5].ni[4].nvs" 18304;
	setAttr ".tgi[5].ni[5].x" 1098.5714111328125;
	setAttr ".tgi[5].ni[5].y" 1090;
	setAttr ".tgi[5].ni[5].nvs" 18304;
	setAttr ".tgi[5].ni[6].x" 1405.7142333984375;
	setAttr ".tgi[5].ni[6].y" 1082.857177734375;
	setAttr ".tgi[5].ni[6].nvs" 18304;
	setAttr ".tgi[5].ni[7].x" 671.4285888671875;
	setAttr ".tgi[5].ni[7].y" 1362.857177734375;
	setAttr ".tgi[5].ni[7].nvs" 18304;
	setAttr ".tgi[5].ni[8].x" 4170;
	setAttr ".tgi[5].ni[8].y" 1045.7142333984375;
	setAttr ".tgi[5].ni[8].nvs" 18304;
	setAttr ".tgi[5].ni[9].x" 2650;
	setAttr ".tgi[5].ni[9].y" 534.28570556640625;
	setAttr ".tgi[5].ni[9].nvs" 18304;
	setAttr ".tgi[5].ni[10].x" -3128.571533203125;
	setAttr ".tgi[5].ni[10].y" 1085.7142333984375;
	setAttr ".tgi[5].ni[10].nvs" 18304;
	setAttr ".tgi[5].ni[11].x" 3555.71435546875;
	setAttr ".tgi[5].ni[11].y" 1052.857177734375;
	setAttr ".tgi[5].ni[11].nvs" 18304;
	setAttr ".tgi[5].ni[12].x" 1405.7142333984375;
	setAttr ".tgi[5].ni[12].y" 984.28570556640625;
	setAttr ".tgi[5].ni[12].nvs" 18304;
	setAttr ".tgi[5].ni[13].x" 667.14288330078125;
	setAttr ".tgi[5].ni[13].y" 1194.2857666015625;
	setAttr ".tgi[5].ni[13].nvs" 18304;
	setAttr ".tgi[5].ni[14].x" 4477.14306640625;
	setAttr ".tgi[5].ni[14].y" 764.28570556640625;
	setAttr ".tgi[5].ni[14].nvs" 18304;
	setAttr ".tgi[5].ni[15].x" 4477.14306640625;
	setAttr ".tgi[5].ni[15].y" 1041.4285888671875;
	setAttr ".tgi[5].ni[15].nvs" 18304;
	setAttr ".tgi[5].ni[16].x" 177.14285278320312;
	setAttr ".tgi[5].ni[16].y" 964.28570556640625;
	setAttr ".tgi[5].ni[16].nvs" 18304;
	setAttr ".tgi[5].ni[17].x" 1712.857177734375;
	setAttr ".tgi[5].ni[17].y" 980;
	setAttr ".tgi[5].ni[17].nvs" 18304;
	setAttr ".tgi[5].ni[18].x" 484.28570556640625;
	setAttr ".tgi[5].ni[18].y" 1101.4285888671875;
	setAttr ".tgi[5].ni[18].nvs" 18304;
	setAttr ".tgi[5].ni[19].x" 2020;
	setAttr ".tgi[5].ni[19].y" 1022.8571166992188;
	setAttr ".tgi[5].ni[19].nvs" 18304;
	setAttr ".tgi[5].ni[20].x" -451.42855834960938;
	setAttr ".tgi[5].ni[20].y" 985.71429443359375;
	setAttr ".tgi[5].ni[20].nvs" 18304;
	setAttr ".tgi[5].ni[21].x" 2327.142822265625;
	setAttr ".tgi[5].ni[21].y" 1018.5714111328125;
	setAttr ".tgi[5].ni[21].nvs" 18304;
	setAttr ".tgi[5].ni[22].x" 580;
	setAttr ".tgi[5].ni[22].y" 622.85711669921875;
	setAttr ".tgi[5].ni[22].nvs" 18304;
	setAttr ".tgi[5].ni[23].x" -437.14285278320312;
	setAttr ".tgi[5].ni[23].y" 855.71429443359375;
	setAttr ".tgi[5].ni[23].nvs" 18304;
	setAttr ".tgi[5].ni[24].x" 791.4285888671875;
	setAttr ".tgi[5].ni[24].y" 1045.7142333984375;
	setAttr ".tgi[5].ni[24].nvs" 18304;
	setAttr ".tgi[5].ni[25].x" 3248.571533203125;
	setAttr ".tgi[5].ni[25].y" 1104.2857666015625;
	setAttr ".tgi[5].ni[25].nvs" 18304;
	setAttr ".tgi[5].ni[26].x" -130;
	setAttr ".tgi[5].ni[26].y" 1035.7142333984375;
	setAttr ".tgi[5].ni[26].nvs" 18304;
	setAttr ".tgi[5].ni[27].x" -437.14285278320312;
	setAttr ".tgi[5].ni[27].y" 1084.2857666015625;
	setAttr ".tgi[5].ni[27].nvs" 18304;
	setAttr ".tgi[5].ni[28].x" 3862.857177734375;
	setAttr ".tgi[5].ni[28].y" 1048.5714111328125;
	setAttr ".tgi[5].ni[28].nvs" 18304;
	setAttr ".tgi[5].ni[29].x" 2342.857177734375;
	setAttr ".tgi[5].ni[29].y" 534.28570556640625;
	setAttr ".tgi[5].ni[29].nvs" 18304;
	setAttr ".tgi[5].ni[30].x" 2634.28564453125;
	setAttr ".tgi[5].ni[30].y" 1012.8571166992188;
	setAttr ".tgi[5].ni[30].nvs" 18304;
	setAttr ".tgi[5].ni[31].x" 1098.5714111328125;
	setAttr ".tgi[5].ni[31].y" 991.4285888671875;
	setAttr ".tgi[5].ni[31].nvs" 18304;
	setAttr ".tgi[5].ni[32].x" 2634.28564453125;
	setAttr ".tgi[5].ni[32].y" 1111.4285888671875;
	setAttr ".tgi[5].ni[32].nvs" 18304;
	setAttr ".tgi[5].ni[33].x" -437.14285278320312;
	setAttr ".tgi[5].ni[33].y" 985.71429443359375;
	setAttr ".tgi[5].ni[33].nvs" 18304;
	setAttr ".tgi[5].ni[34].x" -130;
	setAttr ".tgi[5].ni[34].y" 937.14288330078125;
	setAttr ".tgi[5].ni[34].nvs" 18304;
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
	setAttr -s 5 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 7 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 4 ".u";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr -s 5 ".dsm";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :ikSystem;
connectAttr "joint1.s" "joint2.is";
connectAttr "joint2.s" "joint3.is";
connectAttr "joint3.tx" "effector1.tx";
connectAttr "joint3.ty" "effector1.ty";
connectAttr "joint3.tz" "effector1.tz";
connectAttr "joint1.msg" "ikHandle1.hsj";
connectAttr "effector1.hp" "ikHandle1.hee";
connectAttr "ikSCsolver.msg" "ikHandle1.hsv";
connectAttr "start_GRP_parentConstraint1.ctx" "start_GRP.tx";
connectAttr "start_GRP_parentConstraint1.cty" "start_GRP.ty";
connectAttr "start_GRP_parentConstraint1.ctz" "start_GRP.tz";
connectAttr "start_GRP_parentConstraint1.crx" "start_GRP.rx";
connectAttr "start_GRP_parentConstraint1.cry" "start_GRP.ry";
connectAttr "start_GRP_parentConstraint1.crz" "start_GRP.rz";
connectAttr "start_GRP.ro" "start_GRP_parentConstraint1.cro";
connectAttr "start_GRP.pim" "start_GRP_parentConstraint1.cpim";
connectAttr "start_GRP.rp" "start_GRP_parentConstraint1.crp";
connectAttr "start_GRP.rpt" "start_GRP_parentConstraint1.crt";
connectAttr "joint1.t" "start_GRP_parentConstraint1.tg[0].tt";
connectAttr "joint1.rp" "start_GRP_parentConstraint1.tg[0].trp";
connectAttr "joint1.rpt" "start_GRP_parentConstraint1.tg[0].trt";
connectAttr "joint1.r" "start_GRP_parentConstraint1.tg[0].tr";
connectAttr "joint1.ro" "start_GRP_parentConstraint1.tg[0].tro";
connectAttr "joint1.s" "start_GRP_parentConstraint1.tg[0].ts";
connectAttr "joint1.pm" "start_GRP_parentConstraint1.tg[0].tpm";
connectAttr "joint1.jo" "start_GRP_parentConstraint1.tg[0].tjo";
connectAttr "joint1.ssc" "start_GRP_parentConstraint1.tg[0].tsc";
connectAttr "joint1.is" "start_GRP_parentConstraint1.tg[0].tis";
connectAttr "start_GRP_parentConstraint1.w0" "start_GRP_parentConstraint1.tg[0].tw"
		;
connectAttr "end_GRP_parentConstraint1.ctx" "end_GRP.tx";
connectAttr "end_GRP_parentConstraint1.cty" "end_GRP.ty";
connectAttr "end_GRP_parentConstraint1.ctz" "end_GRP.tz";
connectAttr "end_GRP_parentConstraint1.crx" "end_GRP.rx";
connectAttr "end_GRP_parentConstraint1.cry" "end_GRP.ry";
connectAttr "end_GRP_parentConstraint1.crz" "end_GRP.rz";
connectAttr "end_GRP.ro" "end_GRP_parentConstraint1.cro";
connectAttr "end_GRP.pim" "end_GRP_parentConstraint1.cpim";
connectAttr "end_GRP.rp" "end_GRP_parentConstraint1.crp";
connectAttr "end_GRP.rpt" "end_GRP_parentConstraint1.crt";
connectAttr "locator1.t" "end_GRP_parentConstraint1.tg[0].tt";
connectAttr "locator1.rp" "end_GRP_parentConstraint1.tg[0].trp";
connectAttr "locator1.rpt" "end_GRP_parentConstraint1.tg[0].trt";
connectAttr "locator1.r" "end_GRP_parentConstraint1.tg[0].tr";
connectAttr "locator1.ro" "end_GRP_parentConstraint1.tg[0].tro";
connectAttr "locator1.s" "end_GRP_parentConstraint1.tg[0].ts";
connectAttr "locator1.pm" "end_GRP_parentConstraint1.tg[0].tpm";
connectAttr "end_GRP_parentConstraint1.w0" "end_GRP_parentConstraint1.tg[0].tw";
connectAttr "cluster6.og[0]" "curveShape1.cr";
connectAttr "tweak2.pl[0].cp[0]" "curveShape1.twl";
connectAttr "cluster5GroupId.id" "curveShape1.iog.og[0].gid";
connectAttr "cluster5Set.mwc" "curveShape1.iog.og[0].gco";
connectAttr "groupId4.id" "curveShape1.iog.og[1].gid";
connectAttr "tweakSet2.mwc" "curveShape1.iog.og[1].gco";
connectAttr "cluster6GroupId.id" "curveShape1.iog.og[3].gid";
connectAttr "cluster6Set.mwc" "curveShape1.iog.og[3].gco";
connectAttr "test_poc_010.p" "bezier_aim_RVT.t";
connectAttr "bezier_aim_RVT_aimConstraint1.cr" "bezier_aim_RVT.r";
connectAttr "test_poc_010.t" "bezier_aim_RVT_aimConstraint1.tg[0].tt";
connectAttr "test_pma_010.o3" "bezier_aim_RVT_aimConstraint1.wu";
connectAttr "decompose_mtx_NOD12.ot" "|cartoony_GRP|lower_GRP|rivet1_OFS.t";
connectAttr "decompose_mtx_NOD12.or" "|cartoony_GRP|lower_GRP|rivet1_OFS.r";
connectAttr "decompose_mtx_NOD12.os" "|cartoony_GRP|lower_GRP|rivet1_OFS.s";
connectAttr "decompose_mtx_NOD13.ot" "|cartoony_GRP|lower_GRP|rivet2_OFS.t";
connectAttr "decompose_mtx_NOD13.or" "|cartoony_GRP|lower_GRP|rivet2_OFS.r";
connectAttr "decompose_mtx_NOD13.os" "|cartoony_GRP|lower_GRP|rivet2_OFS.s";
connectAttr "decompose_mtx_NOD14.ot" "|cartoony_GRP|lower_GRP|rivet3_OFS.t";
connectAttr "decompose_mtx_NOD14.or" "|cartoony_GRP|lower_GRP|rivet3_OFS.r";
connectAttr "decompose_mtx_NOD14.os" "|cartoony_GRP|lower_GRP|rivet3_OFS.s";
connectAttr "decompose_mtx_NOD15.ot" "|cartoony_GRP|lower_GRP|rivet4_OFS.t";
connectAttr "decompose_mtx_NOD15.or" "|cartoony_GRP|lower_GRP|rivet4_OFS.r";
connectAttr "decompose_mtx_NOD15.os" "|cartoony_GRP|lower_GRP|rivet4_OFS.s";
connectAttr "decompose_mtx_NOD16.ot" "|cartoony_GRP|lower_GRP|rivet5_OFS.t";
connectAttr "decompose_mtx_NOD16.or" "|cartoony_GRP|lower_GRP|rivet5_OFS.r";
connectAttr "decompose_mtx_NOD16.os" "|cartoony_GRP|lower_GRP|rivet5_OFS.s";
connectAttr "decompose_mtx_NOD17.ot" "|cartoony_GRP|lower_GRP|rivet6_OFS.t";
connectAttr "decompose_mtx_NOD17.or" "|cartoony_GRP|lower_GRP|rivet6_OFS.r";
connectAttr "decompose_mtx_NOD17.os" "|cartoony_GRP|lower_GRP|rivet6_OFS.s";
connectAttr "decompose_mtx_NOD18.ot" "|cartoony_GRP|lower_GRP|rivet7_OFS.t";
connectAttr "decompose_mtx_NOD18.or" "|cartoony_GRP|lower_GRP|rivet7_OFS.r";
connectAttr "decompose_mtx_NOD18.os" "|cartoony_GRP|lower_GRP|rivet7_OFS.s";
connectAttr "decompose_mtx_NOD19.ot" "|cartoony_GRP|lower_GRP|rivet8_OFS.t";
connectAttr "decompose_mtx_NOD19.or" "|cartoony_GRP|lower_GRP|rivet8_OFS.r";
connectAttr "decompose_mtx_NOD19.os" "|cartoony_GRP|lower_GRP|rivet8_OFS.s";
connectAttr "decompose_mtx_NOD20.ot" "|cartoony_GRP|lower_GRP|rivet9_OFS.t";
connectAttr "decompose_mtx_NOD20.or" "|cartoony_GRP|lower_GRP|rivet9_OFS.r";
connectAttr "decompose_mtx_NOD20.os" "|cartoony_GRP|lower_GRP|rivet9_OFS.s";
connectAttr "decompose_mtx_NOD21.ot" "|cartoony_GRP|lower_GRP|rivet10_OFS.t";
connectAttr "decompose_mtx_NOD21.or" "|cartoony_GRP|lower_GRP|rivet10_OFS.r";
connectAttr "decompose_mtx_NOD21.os" "|cartoony_GRP|lower_GRP|rivet10_OFS.s";
connectAttr "tweakSet4.mwc" "nurbsPlaneShape2.iog.og[1].gco";
connectAttr "groupId24.id" "nurbsPlaneShape2.iog.og[1].gid";
connectAttr "ffd1GroupId1.id" "nurbsPlaneShape2.iog.og[4].gid";
connectAttr "ffd1Set1.mwc" "nurbsPlaneShape2.iog.og[4].gco";
connectAttr "ffd2.og[0]" "nurbsPlaneShape2.cr";
connectAttr "tweak4.pl[0].cp[0]" "nurbsPlaneShape2.twl";
connectAttr "makeNurbPlane2.os" "nurbsPlaneShape1Orig2.cr";
connectAttr "skinCluster1GroupId1.id" "ffd1Lattice1Shape.iog.og[0].gid";
connectAttr "skinCluster1Set1.mwc" "ffd1Lattice1Shape.iog.og[0].gco";
connectAttr "groupId25.id" "ffd1Lattice1Shape.iog.og[1].gid";
connectAttr "tweakSet5.mwc" "ffd1Lattice1Shape.iog.og[1].gco";
connectAttr "skinCluster2.og[0]" "ffd1Lattice1Shape.li";
connectAttr "tweak5.pl[0].cp[0]" "ffd1Lattice1Shape.twl";
connectAttr "rebuildCurve4.oc" "duplicatedCurveShape5.cr";
connectAttr "rebuildCurve3.oc" "duplicatedCurveShape4.cr";
connectAttr "rebuildSurface2.os" "loftedSurfaceShape2.cr";
connectAttr "decompose_mtx_NOD2.ot" "|cartoony_GRP|upper_GRP|rivet1_OFS.t";
connectAttr "decompose_mtx_NOD2.or" "|cartoony_GRP|upper_GRP|rivet1_OFS.r";
connectAttr "decompose_mtx_NOD2.os" "|cartoony_GRP|upper_GRP|rivet1_OFS.s";
connectAttr "decompose_mtx_NOD3.ot" "|cartoony_GRP|upper_GRP|rivet2_OFS.t";
connectAttr "decompose_mtx_NOD3.or" "|cartoony_GRP|upper_GRP|rivet2_OFS.r";
connectAttr "decompose_mtx_NOD3.os" "|cartoony_GRP|upper_GRP|rivet2_OFS.s";
connectAttr "decompose_mtx_NOD4.ot" "|cartoony_GRP|upper_GRP|rivet3_OFS.t";
connectAttr "decompose_mtx_NOD4.or" "|cartoony_GRP|upper_GRP|rivet3_OFS.r";
connectAttr "decompose_mtx_NOD4.os" "|cartoony_GRP|upper_GRP|rivet3_OFS.s";
connectAttr "decompose_mtx_NOD5.ot" "|cartoony_GRP|upper_GRP|rivet4_OFS.t";
connectAttr "decompose_mtx_NOD5.or" "|cartoony_GRP|upper_GRP|rivet4_OFS.r";
connectAttr "decompose_mtx_NOD5.os" "|cartoony_GRP|upper_GRP|rivet4_OFS.s";
connectAttr "decompose_mtx_NOD6.ot" "|cartoony_GRP|upper_GRP|rivet5_OFS.t";
connectAttr "decompose_mtx_NOD6.or" "|cartoony_GRP|upper_GRP|rivet5_OFS.r";
connectAttr "decompose_mtx_NOD6.os" "|cartoony_GRP|upper_GRP|rivet5_OFS.s";
connectAttr "decompose_mtx_NOD7.ot" "|cartoony_GRP|upper_GRP|rivet6_OFS.t";
connectAttr "decompose_mtx_NOD7.or" "|cartoony_GRP|upper_GRP|rivet6_OFS.r";
connectAttr "decompose_mtx_NOD7.os" "|cartoony_GRP|upper_GRP|rivet6_OFS.s";
connectAttr "decompose_mtx_NOD8.ot" "|cartoony_GRP|upper_GRP|rivet7_OFS.t";
connectAttr "decompose_mtx_NOD8.or" "|cartoony_GRP|upper_GRP|rivet7_OFS.r";
connectAttr "decompose_mtx_NOD8.os" "|cartoony_GRP|upper_GRP|rivet7_OFS.s";
connectAttr "decompose_mtx_NOD9.ot" "|cartoony_GRP|upper_GRP|rivet8_OFS.t";
connectAttr "decompose_mtx_NOD9.or" "|cartoony_GRP|upper_GRP|rivet8_OFS.r";
connectAttr "decompose_mtx_NOD9.os" "|cartoony_GRP|upper_GRP|rivet8_OFS.s";
connectAttr "decompose_mtx_NOD10.ot" "|cartoony_GRP|upper_GRP|rivet9_OFS.t";
connectAttr "decompose_mtx_NOD10.or" "|cartoony_GRP|upper_GRP|rivet9_OFS.r";
connectAttr "decompose_mtx_NOD10.os" "|cartoony_GRP|upper_GRP|rivet9_OFS.s";
connectAttr "decompose_mtx_NOD11.ot" "|cartoony_GRP|upper_GRP|rivet10_OFS.t";
connectAttr "decompose_mtx_NOD11.or" "|cartoony_GRP|upper_GRP|rivet10_OFS.r";
connectAttr "decompose_mtx_NOD11.os" "|cartoony_GRP|upper_GRP|rivet10_OFS.s";
connectAttr "tweakSet1.mwc" "nurbsPlaneShape1.iog.og[1].gco";
connectAttr "groupId21.id" "nurbsPlaneShape1.iog.og[1].gid";
connectAttr "ffd1GroupId.id" "nurbsPlaneShape1.iog.og[4].gid";
connectAttr "ffd1Set.mwc" "nurbsPlaneShape1.iog.og[4].gco";
connectAttr "ffd1.og[0]" "nurbsPlaneShape1.cr";
connectAttr "tweak1.pl[0].cp[0]" "nurbsPlaneShape1.twl";
connectAttr "makeNurbPlane1.os" "nurbsPlaneShape1Orig.cr";
connectAttr "skinCluster1.og[0]" "ffd1LatticeShape.li";
connectAttr "tweak3.pl[0].cp[0]" "ffd1LatticeShape.twl";
connectAttr "skinCluster1GroupId.id" "ffd1LatticeShape.iog.og[0].gid";
connectAttr "skinCluster1Set.mwc" "ffd1LatticeShape.iog.og[0].gco";
connectAttr "groupId23.id" "ffd1LatticeShape.iog.og[1].gid";
connectAttr "tweakSet3.mwc" "ffd1LatticeShape.iog.og[1].gco";
connectAttr "rebuildCurve1.oc" "duplicatedCurveShape1.cr";
connectAttr "rebuildCurve2.oc" "duplicatedCurveShape2.cr";
connectAttr "rebuildSurface1.os" "loftedSurfaceShape1.cr";
connectAttr "upper_start_parentConstraint1.ctx" "upper_start.tx";
connectAttr "upper_start_parentConstraint1.cty" "upper_start.ty";
connectAttr "upper_start_parentConstraint1.ctz" "upper_start.tz";
connectAttr "upper_start_parentConstraint1.crx" "upper_start.rx";
connectAttr "upper_start_parentConstraint1.cry" "upper_start.ry";
connectAttr "upper_start_parentConstraint1.crz" "upper_start.rz";
connectAttr "upper_start.ro" "upper_start_parentConstraint1.cro";
connectAttr "upper_start.pim" "upper_start_parentConstraint1.cpim";
connectAttr "upper_start.rp" "upper_start_parentConstraint1.crp";
connectAttr "upper_start.rpt" "upper_start_parentConstraint1.crt";
connectAttr "upper_start.jo" "upper_start_parentConstraint1.cjo";
connectAttr "upper_cartoony_CON.t" "upper_start_parentConstraint1.tg[0].tt";
connectAttr "upper_cartoony_CON.rp" "upper_start_parentConstraint1.tg[0].trp";
connectAttr "upper_cartoony_CON.rpt" "upper_start_parentConstraint1.tg[0].trt";
connectAttr "upper_cartoony_CON.r" "upper_start_parentConstraint1.tg[0].tr";
connectAttr "upper_cartoony_CON.ro" "upper_start_parentConstraint1.tg[0].tro";
connectAttr "upper_cartoony_CON.s" "upper_start_parentConstraint1.tg[0].ts";
connectAttr "upper_cartoony_CON.pm" "upper_start_parentConstraint1.tg[0].tpm";
connectAttr "upper_start_parentConstraint1.w0" "upper_start_parentConstraint1.tg[0].tw"
		;
connectAttr "upper_mid_parentConstraint1.ctx" "upper_mid.tx";
connectAttr "upper_mid_parentConstraint1.cty" "upper_mid.ty";
connectAttr "upper_mid_parentConstraint1.ctz" "upper_mid.tz";
connectAttr "upper_mid_parentConstraint1.crx" "upper_mid.rx";
connectAttr "upper_mid_parentConstraint1.cry" "upper_mid.ry";
connectAttr "upper_mid_parentConstraint1.crz" "upper_mid.rz";
connectAttr "upper_mid.ro" "upper_mid_parentConstraint1.cro";
connectAttr "upper_mid.pim" "upper_mid_parentConstraint1.cpim";
connectAttr "upper_mid.rp" "upper_mid_parentConstraint1.crp";
connectAttr "upper_mid.rpt" "upper_mid_parentConstraint1.crt";
connectAttr "upper_mid.jo" "upper_mid_parentConstraint1.cjo";
connectAttr "bezierHandleA_CON.t" "upper_mid_parentConstraint1.tg[0].tt";
connectAttr "bezierHandleA_CON.rp" "upper_mid_parentConstraint1.tg[0].trp";
connectAttr "bezierHandleA_CON.rpt" "upper_mid_parentConstraint1.tg[0].trt";
connectAttr "bezierHandleA_CON.r" "upper_mid_parentConstraint1.tg[0].tr";
connectAttr "bezierHandleA_CON.ro" "upper_mid_parentConstraint1.tg[0].tro";
connectAttr "bezierHandleA_CON.s" "upper_mid_parentConstraint1.tg[0].ts";
connectAttr "bezierHandleA_CON.pm" "upper_mid_parentConstraint1.tg[0].tpm";
connectAttr "upper_mid_parentConstraint1.w0" "upper_mid_parentConstraint1.tg[0].tw"
		;
connectAttr "upper_end_parentConstraint1.ctx" "upper_end.tx";
connectAttr "upper_end_parentConstraint1.cty" "upper_end.ty";
connectAttr "upper_end_parentConstraint1.ctz" "upper_end.tz";
connectAttr "upper_end_parentConstraint1.crx" "upper_end.rx";
connectAttr "upper_end_parentConstraint1.cry" "upper_end.ry";
connectAttr "upper_end_parentConstraint1.crz" "upper_end.rz";
connectAttr "upper_end.ro" "upper_end_parentConstraint1.cro";
connectAttr "upper_end.pim" "upper_end_parentConstraint1.cpim";
connectAttr "upper_end.rp" "upper_end_parentConstraint1.crp";
connectAttr "upper_end.rpt" "upper_end_parentConstraint1.crt";
connectAttr "upper_end.jo" "upper_end_parentConstraint1.cjo";
connectAttr "bezier_CON.t" "upper_end_parentConstraint1.tg[0].tt";
connectAttr "bezier_CON.rp" "upper_end_parentConstraint1.tg[0].trp";
connectAttr "bezier_CON.rpt" "upper_end_parentConstraint1.tg[0].trt";
connectAttr "bezier_CON.r" "upper_end_parentConstraint1.tg[0].tr";
connectAttr "bezier_CON.ro" "upper_end_parentConstraint1.tg[0].tro";
connectAttr "bezier_CON.s" "upper_end_parentConstraint1.tg[0].ts";
connectAttr "bezier_CON.pm" "upper_end_parentConstraint1.tg[0].tpm";
connectAttr "upper_end_parentConstraint1.w0" "upper_end_parentConstraint1.tg[0].tw"
		;
connectAttr "lower_mid_parentConstraint1.ctx" "lower_mid.tx";
connectAttr "lower_mid_parentConstraint1.cty" "lower_mid.ty";
connectAttr "lower_mid_parentConstraint1.ctz" "lower_mid.tz";
connectAttr "lower_mid_parentConstraint1.crx" "lower_mid.rx";
connectAttr "lower_mid_parentConstraint1.cry" "lower_mid.ry";
connectAttr "lower_mid_parentConstraint1.crz" "lower_mid.rz";
connectAttr "lower_mid.ro" "lower_mid_parentConstraint1.cro";
connectAttr "lower_mid.pim" "lower_mid_parentConstraint1.cpim";
connectAttr "lower_mid.rp" "lower_mid_parentConstraint1.crp";
connectAttr "lower_mid.rpt" "lower_mid_parentConstraint1.crt";
connectAttr "lower_mid.jo" "lower_mid_parentConstraint1.cjo";
connectAttr "bezierHandleB_CON.t" "lower_mid_parentConstraint1.tg[0].tt";
connectAttr "bezierHandleB_CON.rp" "lower_mid_parentConstraint1.tg[0].trp";
connectAttr "bezierHandleB_CON.rpt" "lower_mid_parentConstraint1.tg[0].trt";
connectAttr "bezierHandleB_CON.r" "lower_mid_parentConstraint1.tg[0].tr";
connectAttr "bezierHandleB_CON.ro" "lower_mid_parentConstraint1.tg[0].tro";
connectAttr "bezierHandleB_CON.s" "lower_mid_parentConstraint1.tg[0].ts";
connectAttr "bezierHandleB_CON.pm" "lower_mid_parentConstraint1.tg[0].tpm";
connectAttr "lower_mid_parentConstraint1.w0" "lower_mid_parentConstraint1.tg[0].tw"
		;
connectAttr "lower_start_parentConstraint1.ctx" "lower_start.tx";
connectAttr "lower_start_parentConstraint1.cty" "lower_start.ty";
connectAttr "lower_start_parentConstraint1.ctz" "lower_start.tz";
connectAttr "lower_start_parentConstraint1.crx" "lower_start.rx";
connectAttr "lower_start_parentConstraint1.cry" "lower_start.ry";
connectAttr "lower_start_parentConstraint1.crz" "lower_start.rz";
connectAttr "lower_start.ro" "lower_start_parentConstraint1.cro";
connectAttr "lower_start.pim" "lower_start_parentConstraint1.cpim";
connectAttr "lower_start.rp" "lower_start_parentConstraint1.crp";
connectAttr "lower_start.rpt" "lower_start_parentConstraint1.crt";
connectAttr "lower_start.jo" "lower_start_parentConstraint1.cjo";
connectAttr "bezier_CON.t" "lower_start_parentConstraint1.tg[0].tt";
connectAttr "bezier_CON.rp" "lower_start_parentConstraint1.tg[0].trp";
connectAttr "bezier_CON.rpt" "lower_start_parentConstraint1.tg[0].trt";
connectAttr "bezier_CON.r" "lower_start_parentConstraint1.tg[0].tr";
connectAttr "bezier_CON.ro" "lower_start_parentConstraint1.tg[0].tro";
connectAttr "bezier_CON.s" "lower_start_parentConstraint1.tg[0].ts";
connectAttr "bezier_CON.pm" "lower_start_parentConstraint1.tg[0].tpm";
connectAttr "lower_start_parentConstraint1.w0" "lower_start_parentConstraint1.tg[0].tw"
		;
connectAttr "lower_end_parentConstraint1.ctx" "lower_end.tx";
connectAttr "lower_end_parentConstraint1.cty" "lower_end.ty";
connectAttr "lower_end_parentConstraint1.ctz" "lower_end.tz";
connectAttr "lower_end_parentConstraint1.crx" "lower_end.rx";
connectAttr "lower_end_parentConstraint1.cry" "lower_end.ry";
connectAttr "lower_end_parentConstraint1.crz" "lower_end.rz";
connectAttr "lower_end.ro" "lower_end_parentConstraint1.cro";
connectAttr "lower_end.pim" "lower_end_parentConstraint1.cpim";
connectAttr "lower_end.rp" "lower_end_parentConstraint1.crp";
connectAttr "lower_end.rpt" "lower_end_parentConstraint1.crt";
connectAttr "lower_end.jo" "lower_end_parentConstraint1.cjo";
connectAttr "lower_cartoony_CON.t" "lower_end_parentConstraint1.tg[0].tt";
connectAttr "lower_cartoony_CON.rp" "lower_end_parentConstraint1.tg[0].trp";
connectAttr "lower_cartoony_CON.rpt" "lower_end_parentConstraint1.tg[0].trt";
connectAttr "lower_cartoony_CON.r" "lower_end_parentConstraint1.tg[0].tr";
connectAttr "lower_cartoony_CON.ro" "lower_end_parentConstraint1.tg[0].tro";
connectAttr "lower_cartoony_CON.s" "lower_end_parentConstraint1.tg[0].ts";
connectAttr "lower_cartoony_CON.pm" "lower_end_parentConstraint1.tg[0].tpm";
connectAttr "lower_end_parentConstraint1.w0" "lower_end_parentConstraint1.tg[0].tw"
		;
connectAttr "test_a_line_001_dm_001.ot" "a_lineShape.cp[0]";
connectAttr "test_a_line_001_dm_002.ot" "a_lineShape.cp[1]";
connectAttr "test_b_line_000_dm_003.ot" "b_line0Shape.cp[0]";
connectAttr "test_a_line_000_dm_002.ot" "b_line0Shape.cp[1]";
connectAttr "skinCluster3GroupId.id" "pCylinderShape1.iog.og[0].gid";
connectAttr "skinCluster3Set.mwc" "pCylinderShape1.iog.og[0].gco";
connectAttr "groupId27.id" "pCylinderShape1.iog.og[1].gid";
connectAttr "tweakSet6.mwc" "pCylinderShape1.iog.og[1].gco";
connectAttr "skinCluster3.og[0]" "pCylinderShape1.i";
connectAttr "tweak6.vl[0].vt[0]" "pCylinderShape1.twl";
connectAttr "transformGeometry1.og" "pCylinderShape1Orig.i";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert2SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert3SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert4SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert2SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert3SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert4SG.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "test_slide_shift_clamp.opr" "test_slide_shift_mdl.i2";
connectAttr "cluster5GroupParts.og" "cluster5.ip[0].ig";
connectAttr "cluster5GroupId.id" "cluster5.ip[0].gi";
connectAttr "cluster5Handle.wm" "cluster5.ma";
connectAttr "cluster5HandleShape.x" "cluster5.x";
connectAttr "groupParts4.og" "tweak2.ip[0].ig";
connectAttr "groupId4.id" "tweak2.ip[0].gi";
connectAttr "cluster5GroupId.msg" "cluster5Set.gn" -na;
connectAttr "curveShape1.iog.og[0]" "cluster5Set.dsm" -na;
connectAttr "cluster5.msg" "cluster5Set.ub[0]";
connectAttr "tweak2.og[0]" "cluster5GroupParts.ig";
connectAttr "cluster5GroupId.id" "cluster5GroupParts.gi";
connectAttr "groupId4.msg" "tweakSet2.gn" -na;
connectAttr "curveShape1.iog.og[1]" "tweakSet2.dsm" -na;
connectAttr "tweak2.msg" "tweakSet2.ub[0]";
connectAttr "curveShape1Orig.ws" "groupParts4.ig";
connectAttr "groupId4.id" "groupParts4.gi";
connectAttr "end_read_NUL.wm" "test_bm_010.i[0].m";
connectAttr "start_read_NUL.wm" "test_bm_010.i[1].m";
connectAttr "test_bm_010.o" "test_up_pmm_010.im";
connectAttr "test_bm_010.o" "test_up_dm_010.imat";
connectAttr "test_up_pmm_010.o" "test_up_pma_010.i3[0]";
connectAttr "test_up_dm_010.ot" "test_up_pma_010.i3[1]";
connectAttr "curveShape1.ws" "test_poc_010.ic";
connectAttr "test_up_pma_010.o3" "test_pma_010.i3[0]";
connectAttr "test_poc_010.p" "test_pma_010.i3[1]";
connectAttr "test_slide_shift_clamp1.opr" "test_slide_shift_mdl1.i2";
connectAttr "test_slide_uv_adl_009.o" "test_slide_ramp_009.u";
connectAttr "test_slide_uv_adl_009.o" "test_slide_ramp_009.v";
connectAttr "test_slide_shift_min_clamp.opr" "test_slide_ramp_009.cel[0].ep";
connectAttr "test_slide_shift_min_clamp.opr" "test_slide_ramp_009.cel[0].ecr";
connectAttr "test_slide_shift_max_clamp.opr" "test_slide_ramp_009.cel[1].ep";
connectAttr "test_slide_shift_max_clamp.opr" "test_slide_ramp_009.cel[1].ecr";
connectAttr "test_slide_shift_clamp1.opr" "test_slide_ramp_009.cel[2].ep";
connectAttr "test_slide_shift_min_clamp.opr" "test_slide_cd_a_009.ft";
connectAttr "test_slide_shift_max_clamp.opr" "test_slide_cd_b_009.ft";
connectAttr "test_slide_cd_a_009.ocr" "test_slide_mdl_009.i1";
connectAttr "test_slide_cd_b_009.ocr" "test_slide_mdl_009.i2";
connectAttr "test_slide_mdl_009.o" "test_slide_cd_c_009.ft";
connectAttr "test_slide_ramp_009.ocr" "test_slide_cd_c_009.cfr";
connectAttr "cluster6GroupParts.og" "cluster6.ip[0].ig";
connectAttr "cluster6GroupId.id" "cluster6.ip[0].gi";
connectAttr "cluster6Handle.wm" "cluster6.ma";
connectAttr "cluster6HandleShape.x" "cluster6.x";
connectAttr "cluster6GroupId.msg" "cluster6Set.gn" -na;
connectAttr "curveShape1.iog.og[3]" "cluster6Set.dsm" -na;
connectAttr "cluster6.msg" "cluster6Set.ub[0]";
connectAttr "cluster5.og[0]" "cluster6GroupParts.ig";
connectAttr "cluster6GroupId.id" "cluster6GroupParts.gi";
connectAttr "curveShape1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn";
connectAttr "bezier_aim_RVT_aimConstraint1.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[0].dn"
		;
connectAttr "test_poc_010.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[1].dn";
connectAttr "upv_LOCShape.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[2].dn";
connectAttr "aim_LOC.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[3].dn";
connectAttr "cluster6.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[4].dn";
connectAttr "cluster6HandleShape.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[5].dn"
		;
connectAttr "curveShape1Orig.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[6].dn";
connectAttr "bezier_aim_GRP.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[7].dn";
connectAttr "start_GRP.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[8].dn";
connectAttr "cluster5HandleShape.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[9].dn"
		;
connectAttr "start_read_NUL.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[10].dn";
connectAttr "test_bm_010.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[11].dn";
connectAttr "curveShape1.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[12].dn";
connectAttr "test_up_dm_010.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[13].dn";
connectAttr "bezier_aim_RVT.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[14].dn";
connectAttr "end_GRP_parentConstraint1.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[15].dn"
		;
connectAttr "cluster5.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[16].dn";
connectAttr "aim_LOCShape.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[17].dn";
connectAttr "upv_LOC.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[18].dn";
connectAttr "cluster6Set.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[19].dn";
connectAttr "end_GRP.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[20].dn";
connectAttr "tweak2.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[21].dn";
connectAttr "test_up_pma_010.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[22].dn"
		;
connectAttr "cluster5Handle.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[23].dn";
connectAttr "test_up_pmm_010.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[24].dn"
		;
connectAttr "test_pma_010.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[25].dn";
connectAttr "end_read_NUL.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[26].dn";
connectAttr "cluster6Handle.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[27].dn";
connectAttr "start_GRP_parentConstraint1.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[28].dn"
		;
connectAttr "lambert2.oc" "lambert2SG.ss";
connectAttr "lambert2SG.msg" "materialInfo1.sg";
connectAttr "lambert2.msg" "materialInfo1.m";
connectAttr "lambert3.oc" "lambert3SG.ss";
connectAttr "lambert3SG.msg" "materialInfo2.sg";
connectAttr "lambert3.msg" "materialInfo2.m";
connectAttr "lambert4.oc" "lambert4SG.ss";
connectAttr "lambert4SG.msg" "materialInfo3.sg";
connectAttr "lambert4.msg" "materialInfo3.m";
connectAttr "groupParts18.og" "tweak1.ip[0].ig";
connectAttr "groupId21.id" "tweak1.ip[0].gi";
connectAttr "nurbsPlaneShape1Orig.ws" "groupParts18.ig";
connectAttr "groupId21.id" "groupParts18.gi";
connectAttr "groupId21.msg" "tweakSet1.gn" -na;
connectAttr "nurbsPlaneShape1.iog.og[1]" "tweakSet1.dsm" -na;
connectAttr "tweak1.msg" "tweakSet1.ub[0]";
connectAttr "ffd1GroupParts.og" "ffd1.ip[0].ig";
connectAttr "ffd1GroupId.id" "ffd1.ip[0].gi";
connectAttr "ffd1LatticeShape.wm" "ffd1.dlm";
connectAttr "ffd1LatticeShape.lo" "ffd1.dlp";
connectAttr "ffd1BaseShape.wm" "ffd1.blm";
connectAttr "ffd1GroupId.msg" "ffd1Set.gn" -na;
connectAttr "nurbsPlaneShape1.iog.og[4]" "ffd1Set.dsm" -na;
connectAttr "ffd1.msg" "ffd1Set.ub[0]";
connectAttr "tweak1.og[0]" "ffd1GroupParts.ig";
connectAttr "ffd1GroupId.id" "ffd1GroupParts.gi";
connectAttr "skinCluster1GroupParts.og" "skinCluster1.ip[0].ig";
connectAttr "skinCluster1GroupId.id" "skinCluster1.ip[0].gi";
connectAttr "bindPose1.msg" "skinCluster1.bp";
connectAttr "upper_start.wm" "skinCluster1.ma[0]";
connectAttr "upper_mid.wm" "skinCluster1.ma[1]";
connectAttr "upper_end.wm" "skinCluster1.ma[2]";
connectAttr "upper_start.liw" "skinCluster1.lw[0]";
connectAttr "upper_mid.liw" "skinCluster1.lw[1]";
connectAttr "upper_end.liw" "skinCluster1.lw[2]";
connectAttr "upper_start.obcc" "skinCluster1.ifcl[0]";
connectAttr "upper_mid.obcc" "skinCluster1.ifcl[1]";
connectAttr "upper_end.obcc" "skinCluster1.ifcl[2]";
connectAttr "groupParts20.og" "tweak3.ip[0].ig";
connectAttr "groupId23.id" "tweak3.ip[0].gi";
connectAttr "skinCluster1GroupId.msg" "skinCluster1Set.gn" -na;
connectAttr "ffd1LatticeShape.iog.og[0]" "skinCluster1Set.dsm" -na;
connectAttr "skinCluster1.msg" "skinCluster1Set.ub[0]";
connectAttr "tweak3.og[0]" "skinCluster1GroupParts.ig";
connectAttr "skinCluster1GroupId.id" "skinCluster1GroupParts.gi";
connectAttr "groupId23.msg" "tweakSet3.gn" -na;
connectAttr "ffd1LatticeShape.iog.og[1]" "tweakSet3.dsm" -na;
connectAttr "tweak3.msg" "tweakSet3.ub[0]";
connectAttr "ffd1LatticeShapeOrig.wl" "groupParts20.ig";
connectAttr "groupId23.id" "groupParts20.gi";
connectAttr "upper_start.msg" "bindPose1.m[0]";
connectAttr "upper_mid.msg" "bindPose1.m[1]";
connectAttr "upper_end.msg" "bindPose1.m[2]";
connectAttr "bindPose1.w" "bindPose1.p[0]";
connectAttr "bindPose1.w" "bindPose1.p[1]";
connectAttr "bindPose1.w" "bindPose1.p[2]";
connectAttr "upper_start.bps" "bindPose1.wm[0]";
connectAttr "upper_mid.bps" "bindPose1.wm[1]";
connectAttr "upper_end.bps" "bindPose1.wm[2]";
connectAttr "nurbsPlaneShape1.ws" "curveFromSurfaceIso1.is";
connectAttr "nurbsPlaneShape1.ws" "curveFromSurfaceIso2.is";
connectAttr "curveFromSurfaceIso1.oc" "rebuildCurve1.ic";
connectAttr "curveFromSurfaceIso2.oc" "rebuildCurve2.ic";
connectAttr "duplicatedCurveShape2.ws" "loft1.ic[0]";
connectAttr "duplicatedCurveShape1.ws" "loft1.ic[1]";
connectAttr "loft1.os" "rebuildSurface1.is";
connectAttr "compose_mtx_NOD2.o" "decompose_mtx_NOD2.imat";
connectAttr "xy_axis_NOD2.nnx" "compose_mtx_NOD2.i00";
connectAttr "xy_axis_NOD2.nny" "compose_mtx_NOD2.i01";
connectAttr "xy_axis_NOD2.nnz" "compose_mtx_NOD2.i02";
connectAttr "xy_axis_NOD2.nux" "compose_mtx_NOD2.i10";
connectAttr "xy_axis_NOD2.nuy" "compose_mtx_NOD2.i11";
connectAttr "xy_axis_NOD2.nuz" "compose_mtx_NOD2.i12";
connectAttr "z_axis_NOD2.ox" "compose_mtx_NOD2.i20";
connectAttr "z_axis_NOD2.oy" "compose_mtx_NOD2.i21";
connectAttr "z_axis_NOD2.oz" "compose_mtx_NOD2.i22";
connectAttr "xy_axis_NOD2.px" "compose_mtx_NOD2.i30";
connectAttr "xy_axis_NOD2.py" "compose_mtx_NOD2.i31";
connectAttr "xy_axis_NOD2.pz" "compose_mtx_NOD2.i32";
connectAttr "remapValue1.vl[0].vlfv" "xy_axis_NOD2.u";
connectAttr "loftedSurfaceShape1.ws" "xy_axis_NOD2.is";
connectAttr "xy_axis_NOD2.nn" "z_axis_NOD2.i1";
connectAttr "xy_axis_NOD2.ntu" "z_axis_NOD2.i2";
connectAttr "compose_mtx_NOD3.o" "decompose_mtx_NOD3.imat";
connectAttr "xy_axis_NOD3.nnx" "compose_mtx_NOD3.i00";
connectAttr "xy_axis_NOD3.nny" "compose_mtx_NOD3.i01";
connectAttr "xy_axis_NOD3.nnz" "compose_mtx_NOD3.i02";
connectAttr "xy_axis_NOD3.nux" "compose_mtx_NOD3.i10";
connectAttr "xy_axis_NOD3.nuy" "compose_mtx_NOD3.i11";
connectAttr "xy_axis_NOD3.nuz" "compose_mtx_NOD3.i12";
connectAttr "z_axis_NOD3.ox" "compose_mtx_NOD3.i20";
connectAttr "z_axis_NOD3.oy" "compose_mtx_NOD3.i21";
connectAttr "z_axis_NOD3.oz" "compose_mtx_NOD3.i22";
connectAttr "xy_axis_NOD3.px" "compose_mtx_NOD3.i30";
connectAttr "xy_axis_NOD3.py" "compose_mtx_NOD3.i31";
connectAttr "xy_axis_NOD3.pz" "compose_mtx_NOD3.i32";
connectAttr "remapValue1.vl[1].vlfv" "xy_axis_NOD3.u";
connectAttr "loftedSurfaceShape1.ws" "xy_axis_NOD3.is";
connectAttr "xy_axis_NOD3.nn" "z_axis_NOD3.i1";
connectAttr "xy_axis_NOD3.ntu" "z_axis_NOD3.i2";
connectAttr "compose_mtx_NOD4.o" "decompose_mtx_NOD4.imat";
connectAttr "xy_axis_NOD4.nnx" "compose_mtx_NOD4.i00";
connectAttr "xy_axis_NOD4.nny" "compose_mtx_NOD4.i01";
connectAttr "xy_axis_NOD4.nnz" "compose_mtx_NOD4.i02";
connectAttr "xy_axis_NOD4.nux" "compose_mtx_NOD4.i10";
connectAttr "xy_axis_NOD4.nuy" "compose_mtx_NOD4.i11";
connectAttr "xy_axis_NOD4.nuz" "compose_mtx_NOD4.i12";
connectAttr "z_axis_NOD4.ox" "compose_mtx_NOD4.i20";
connectAttr "z_axis_NOD4.oy" "compose_mtx_NOD4.i21";
connectAttr "z_axis_NOD4.oz" "compose_mtx_NOD4.i22";
connectAttr "xy_axis_NOD4.px" "compose_mtx_NOD4.i30";
connectAttr "xy_axis_NOD4.py" "compose_mtx_NOD4.i31";
connectAttr "xy_axis_NOD4.pz" "compose_mtx_NOD4.i32";
connectAttr "remapValue1.vl[2].vlfv" "xy_axis_NOD4.u";
connectAttr "loftedSurfaceShape1.ws" "xy_axis_NOD4.is";
connectAttr "xy_axis_NOD4.nn" "z_axis_NOD4.i1";
connectAttr "xy_axis_NOD4.ntu" "z_axis_NOD4.i2";
connectAttr "compose_mtx_NOD5.o" "decompose_mtx_NOD5.imat";
connectAttr "xy_axis_NOD5.nnx" "compose_mtx_NOD5.i00";
connectAttr "xy_axis_NOD5.nny" "compose_mtx_NOD5.i01";
connectAttr "xy_axis_NOD5.nnz" "compose_mtx_NOD5.i02";
connectAttr "xy_axis_NOD5.nux" "compose_mtx_NOD5.i10";
connectAttr "xy_axis_NOD5.nuy" "compose_mtx_NOD5.i11";
connectAttr "xy_axis_NOD5.nuz" "compose_mtx_NOD5.i12";
connectAttr "z_axis_NOD5.ox" "compose_mtx_NOD5.i20";
connectAttr "z_axis_NOD5.oy" "compose_mtx_NOD5.i21";
connectAttr "z_axis_NOD5.oz" "compose_mtx_NOD5.i22";
connectAttr "xy_axis_NOD5.px" "compose_mtx_NOD5.i30";
connectAttr "xy_axis_NOD5.py" "compose_mtx_NOD5.i31";
connectAttr "xy_axis_NOD5.pz" "compose_mtx_NOD5.i32";
connectAttr "remapValue1.vl[3].vlfv" "xy_axis_NOD5.u";
connectAttr "loftedSurfaceShape1.ws" "xy_axis_NOD5.is";
connectAttr "xy_axis_NOD5.nn" "z_axis_NOD5.i1";
connectAttr "xy_axis_NOD5.ntu" "z_axis_NOD5.i2";
connectAttr "compose_mtx_NOD6.o" "decompose_mtx_NOD6.imat";
connectAttr "xy_axis_NOD6.nnx" "compose_mtx_NOD6.i00";
connectAttr "xy_axis_NOD6.nny" "compose_mtx_NOD6.i01";
connectAttr "xy_axis_NOD6.nnz" "compose_mtx_NOD6.i02";
connectAttr "xy_axis_NOD6.nux" "compose_mtx_NOD6.i10";
connectAttr "xy_axis_NOD6.nuy" "compose_mtx_NOD6.i11";
connectAttr "xy_axis_NOD6.nuz" "compose_mtx_NOD6.i12";
connectAttr "z_axis_NOD6.ox" "compose_mtx_NOD6.i20";
connectAttr "z_axis_NOD6.oy" "compose_mtx_NOD6.i21";
connectAttr "z_axis_NOD6.oz" "compose_mtx_NOD6.i22";
connectAttr "xy_axis_NOD6.px" "compose_mtx_NOD6.i30";
connectAttr "xy_axis_NOD6.py" "compose_mtx_NOD6.i31";
connectAttr "xy_axis_NOD6.pz" "compose_mtx_NOD6.i32";
connectAttr "remapValue1.vl[4].vlfv" "xy_axis_NOD6.u";
connectAttr "loftedSurfaceShape1.ws" "xy_axis_NOD6.is";
connectAttr "xy_axis_NOD6.nn" "z_axis_NOD6.i1";
connectAttr "xy_axis_NOD6.ntu" "z_axis_NOD6.i2";
connectAttr "compose_mtx_NOD7.o" "decompose_mtx_NOD7.imat";
connectAttr "xy_axis_NOD7.nnx" "compose_mtx_NOD7.i00";
connectAttr "xy_axis_NOD7.nny" "compose_mtx_NOD7.i01";
connectAttr "xy_axis_NOD7.nnz" "compose_mtx_NOD7.i02";
connectAttr "xy_axis_NOD7.nux" "compose_mtx_NOD7.i10";
connectAttr "xy_axis_NOD7.nuy" "compose_mtx_NOD7.i11";
connectAttr "xy_axis_NOD7.nuz" "compose_mtx_NOD7.i12";
connectAttr "z_axis_NOD7.ox" "compose_mtx_NOD7.i20";
connectAttr "z_axis_NOD7.oy" "compose_mtx_NOD7.i21";
connectAttr "z_axis_NOD7.oz" "compose_mtx_NOD7.i22";
connectAttr "xy_axis_NOD7.px" "compose_mtx_NOD7.i30";
connectAttr "xy_axis_NOD7.py" "compose_mtx_NOD7.i31";
connectAttr "xy_axis_NOD7.pz" "compose_mtx_NOD7.i32";
connectAttr "remapValue1.vl[5].vlfv" "xy_axis_NOD7.u";
connectAttr "loftedSurfaceShape1.ws" "xy_axis_NOD7.is";
connectAttr "xy_axis_NOD7.nn" "z_axis_NOD7.i1";
connectAttr "xy_axis_NOD7.ntu" "z_axis_NOD7.i2";
connectAttr "compose_mtx_NOD8.o" "decompose_mtx_NOD8.imat";
connectAttr "xy_axis_NOD8.nnx" "compose_mtx_NOD8.i00";
connectAttr "xy_axis_NOD8.nny" "compose_mtx_NOD8.i01";
connectAttr "xy_axis_NOD8.nnz" "compose_mtx_NOD8.i02";
connectAttr "xy_axis_NOD8.nux" "compose_mtx_NOD8.i10";
connectAttr "xy_axis_NOD8.nuy" "compose_mtx_NOD8.i11";
connectAttr "xy_axis_NOD8.nuz" "compose_mtx_NOD8.i12";
connectAttr "z_axis_NOD8.ox" "compose_mtx_NOD8.i20";
connectAttr "z_axis_NOD8.oy" "compose_mtx_NOD8.i21";
connectAttr "z_axis_NOD8.oz" "compose_mtx_NOD8.i22";
connectAttr "xy_axis_NOD8.px" "compose_mtx_NOD8.i30";
connectAttr "xy_axis_NOD8.py" "compose_mtx_NOD8.i31";
connectAttr "xy_axis_NOD8.pz" "compose_mtx_NOD8.i32";
connectAttr "remapValue1.vl[6].vlfv" "xy_axis_NOD8.u";
connectAttr "loftedSurfaceShape1.ws" "xy_axis_NOD8.is";
connectAttr "xy_axis_NOD8.nn" "z_axis_NOD8.i1";
connectAttr "xy_axis_NOD8.ntu" "z_axis_NOD8.i2";
connectAttr "compose_mtx_NOD9.o" "decompose_mtx_NOD9.imat";
connectAttr "xy_axis_NOD9.nnx" "compose_mtx_NOD9.i00";
connectAttr "xy_axis_NOD9.nny" "compose_mtx_NOD9.i01";
connectAttr "xy_axis_NOD9.nnz" "compose_mtx_NOD9.i02";
connectAttr "xy_axis_NOD9.nux" "compose_mtx_NOD9.i10";
connectAttr "xy_axis_NOD9.nuy" "compose_mtx_NOD9.i11";
connectAttr "xy_axis_NOD9.nuz" "compose_mtx_NOD9.i12";
connectAttr "z_axis_NOD9.ox" "compose_mtx_NOD9.i20";
connectAttr "z_axis_NOD9.oy" "compose_mtx_NOD9.i21";
connectAttr "z_axis_NOD9.oz" "compose_mtx_NOD9.i22";
connectAttr "xy_axis_NOD9.px" "compose_mtx_NOD9.i30";
connectAttr "xy_axis_NOD9.py" "compose_mtx_NOD9.i31";
connectAttr "xy_axis_NOD9.pz" "compose_mtx_NOD9.i32";
connectAttr "remapValue1.vl[7].vlfv" "xy_axis_NOD9.u";
connectAttr "loftedSurfaceShape1.ws" "xy_axis_NOD9.is";
connectAttr "xy_axis_NOD9.nn" "z_axis_NOD9.i1";
connectAttr "xy_axis_NOD9.ntu" "z_axis_NOD9.i2";
connectAttr "compose_mtx_NOD10.o" "decompose_mtx_NOD10.imat";
connectAttr "xy_axis_NOD10.nnx" "compose_mtx_NOD10.i00";
connectAttr "xy_axis_NOD10.nny" "compose_mtx_NOD10.i01";
connectAttr "xy_axis_NOD10.nnz" "compose_mtx_NOD10.i02";
connectAttr "xy_axis_NOD10.nux" "compose_mtx_NOD10.i10";
connectAttr "xy_axis_NOD10.nuy" "compose_mtx_NOD10.i11";
connectAttr "xy_axis_NOD10.nuz" "compose_mtx_NOD10.i12";
connectAttr "z_axis_NOD10.ox" "compose_mtx_NOD10.i20";
connectAttr "z_axis_NOD10.oy" "compose_mtx_NOD10.i21";
connectAttr "z_axis_NOD10.oz" "compose_mtx_NOD10.i22";
connectAttr "xy_axis_NOD10.px" "compose_mtx_NOD10.i30";
connectAttr "xy_axis_NOD10.py" "compose_mtx_NOD10.i31";
connectAttr "xy_axis_NOD10.pz" "compose_mtx_NOD10.i32";
connectAttr "remapValue1.vl[8].vlfv" "xy_axis_NOD10.u";
connectAttr "loftedSurfaceShape1.ws" "xy_axis_NOD10.is";
connectAttr "xy_axis_NOD10.nn" "z_axis_NOD10.i1";
connectAttr "xy_axis_NOD10.ntu" "z_axis_NOD10.i2";
connectAttr "compose_mtx_NOD11.o" "decompose_mtx_NOD11.imat";
connectAttr "xy_axis_NOD11.nnx" "compose_mtx_NOD11.i00";
connectAttr "xy_axis_NOD11.nny" "compose_mtx_NOD11.i01";
connectAttr "xy_axis_NOD11.nnz" "compose_mtx_NOD11.i02";
connectAttr "xy_axis_NOD11.nux" "compose_mtx_NOD11.i10";
connectAttr "xy_axis_NOD11.nuy" "compose_mtx_NOD11.i11";
connectAttr "xy_axis_NOD11.nuz" "compose_mtx_NOD11.i12";
connectAttr "z_axis_NOD11.ox" "compose_mtx_NOD11.i20";
connectAttr "z_axis_NOD11.oy" "compose_mtx_NOD11.i21";
connectAttr "z_axis_NOD11.oz" "compose_mtx_NOD11.i22";
connectAttr "xy_axis_NOD11.px" "compose_mtx_NOD11.i30";
connectAttr "xy_axis_NOD11.py" "compose_mtx_NOD11.i31";
connectAttr "xy_axis_NOD11.pz" "compose_mtx_NOD11.i32";
connectAttr "remapValue1.vl[9].vlfv" "xy_axis_NOD11.u";
connectAttr "loftedSurfaceShape1.ws" "xy_axis_NOD11.is";
connectAttr "xy_axis_NOD11.nn" "z_axis_NOD11.i1";
connectAttr "xy_axis_NOD11.ntu" "z_axis_NOD11.i2";
connectAttr "compose_mtx_NOD12.o" "decompose_mtx_NOD12.imat";
connectAttr "xy_axis_NOD12.nnx" "compose_mtx_NOD12.i00";
connectAttr "xy_axis_NOD12.nny" "compose_mtx_NOD12.i01";
connectAttr "xy_axis_NOD12.nnz" "compose_mtx_NOD12.i02";
connectAttr "xy_axis_NOD12.nux" "compose_mtx_NOD12.i10";
connectAttr "xy_axis_NOD12.nuy" "compose_mtx_NOD12.i11";
connectAttr "xy_axis_NOD12.nuz" "compose_mtx_NOD12.i12";
connectAttr "z_axis_NOD12.ox" "compose_mtx_NOD12.i20";
connectAttr "z_axis_NOD12.oy" "compose_mtx_NOD12.i21";
connectAttr "z_axis_NOD12.oz" "compose_mtx_NOD12.i22";
connectAttr "xy_axis_NOD12.px" "compose_mtx_NOD12.i30";
connectAttr "xy_axis_NOD12.py" "compose_mtx_NOD12.i31";
connectAttr "xy_axis_NOD12.pz" "compose_mtx_NOD12.i32";
connectAttr "remapValue2.vl[0].vlfv" "xy_axis_NOD12.u";
connectAttr "loftedSurfaceShape2.ws" "xy_axis_NOD12.is";
connectAttr "loft2.os" "rebuildSurface2.is";
connectAttr "duplicatedCurveShape4.ws" "loft2.ic[0]";
connectAttr "duplicatedCurveShape5.ws" "loft2.ic[1]";
connectAttr "curveFromSurfaceIso3.oc" "rebuildCurve3.ic";
connectAttr "nurbsPlaneShape2.ws" "curveFromSurfaceIso3.is";
connectAttr "groupId24.msg" "tweakSet4.gn" -na;
connectAttr "nurbsPlaneShape2.iog.og[1]" "tweakSet4.dsm" -na;
connectAttr "tweak4.msg" "tweakSet4.ub[0]";
connectAttr "groupParts21.og" "tweak4.ip[0].ig";
connectAttr "groupId24.id" "tweak4.ip[0].gi";
connectAttr "nurbsPlaneShape1Orig2.ws" "groupParts21.ig";
connectAttr "groupId24.id" "groupParts21.gi";
connectAttr "ffd1GroupId1.msg" "ffd1Set1.gn" -na;
connectAttr "nurbsPlaneShape2.iog.og[4]" "ffd1Set1.dsm" -na;
connectAttr "ffd2.msg" "ffd1Set1.ub[0]";
connectAttr "ffd1GroupParts1.og" "ffd2.ip[0].ig";
connectAttr "ffd1GroupId1.id" "ffd2.ip[0].gi";
connectAttr "ffd1Lattice1Shape.wm" "ffd2.dlm";
connectAttr "ffd1Lattice1Shape.lo" "ffd2.dlp";
connectAttr "ffd1Base1Shape.wm" "ffd2.blm";
connectAttr "skinCluster1GroupParts1.og" "skinCluster2.ip[0].ig";
connectAttr "skinCluster1GroupId1.id" "skinCluster2.ip[0].gi";
connectAttr "bindPose2.msg" "skinCluster2.bp";
connectAttr "lower_start.wm" "skinCluster2.ma[0]";
connectAttr "lower_mid.wm" "skinCluster2.ma[1]";
connectAttr "lower_end.wm" "skinCluster2.ma[2]";
connectAttr "lower_start.liw" "skinCluster2.lw[0]";
connectAttr "lower_mid.liw" "skinCluster2.lw[1]";
connectAttr "lower_end.liw" "skinCluster2.lw[2]";
connectAttr "lower_start.obcc" "skinCluster2.ifcl[0]";
connectAttr "lower_mid.obcc" "skinCluster2.ifcl[1]";
connectAttr "lower_end.obcc" "skinCluster2.ifcl[2]";
connectAttr "lower_start.msg" "bindPose2.m[0]";
connectAttr "lower_mid.msg" "bindPose2.m[1]";
connectAttr "lower_end.msg" "bindPose2.m[2]";
connectAttr "bindPose2.w" "bindPose2.p[0]";
connectAttr "bindPose2.w" "bindPose2.p[1]";
connectAttr "bindPose2.w" "bindPose2.p[2]";
connectAttr "lower_start.bps" "bindPose2.wm[0]";
connectAttr "lower_mid.bps" "bindPose2.wm[1]";
connectAttr "lower_end.bps" "bindPose2.wm[2]";
connectAttr "skinCluster1GroupId1.msg" "skinCluster1Set1.gn" -na;
connectAttr "ffd1Lattice1Shape.iog.og[0]" "skinCluster1Set1.dsm" -na;
connectAttr "skinCluster2.msg" "skinCluster1Set1.ub[0]";
connectAttr "tweak5.og[0]" "skinCluster1GroupParts1.ig";
connectAttr "skinCluster1GroupId1.id" "skinCluster1GroupParts1.gi";
connectAttr "groupParts22.og" "tweak5.ip[0].ig";
connectAttr "groupId25.id" "tweak5.ip[0].gi";
connectAttr "groupId25.msg" "tweakSet5.gn" -na;
connectAttr "ffd1Lattice1Shape.iog.og[1]" "tweakSet5.dsm" -na;
connectAttr "tweak5.msg" "tweakSet5.ub[0]";
connectAttr "ffd1Lattice1ShapeOrig.wl" "groupParts22.ig";
connectAttr "groupId25.id" "groupParts22.gi";
connectAttr "tweak4.og[0]" "ffd1GroupParts1.ig";
connectAttr "ffd1GroupId1.id" "ffd1GroupParts1.gi";
connectAttr "curveFromSurfaceIso4.oc" "rebuildCurve4.ic";
connectAttr "nurbsPlaneShape2.ws" "curveFromSurfaceIso4.is";
connectAttr "xy_axis_NOD12.nn" "z_axis_NOD12.i1";
connectAttr "xy_axis_NOD12.ntu" "z_axis_NOD12.i2";
connectAttr "compose_mtx_NOD13.o" "decompose_mtx_NOD13.imat";
connectAttr "xy_axis_NOD13.nnx" "compose_mtx_NOD13.i00";
connectAttr "xy_axis_NOD13.nny" "compose_mtx_NOD13.i01";
connectAttr "xy_axis_NOD13.nnz" "compose_mtx_NOD13.i02";
connectAttr "xy_axis_NOD13.nux" "compose_mtx_NOD13.i10";
connectAttr "xy_axis_NOD13.nuy" "compose_mtx_NOD13.i11";
connectAttr "xy_axis_NOD13.nuz" "compose_mtx_NOD13.i12";
connectAttr "z_axis_NOD13.ox" "compose_mtx_NOD13.i20";
connectAttr "z_axis_NOD13.oy" "compose_mtx_NOD13.i21";
connectAttr "z_axis_NOD13.oz" "compose_mtx_NOD13.i22";
connectAttr "xy_axis_NOD13.px" "compose_mtx_NOD13.i30";
connectAttr "xy_axis_NOD13.py" "compose_mtx_NOD13.i31";
connectAttr "xy_axis_NOD13.pz" "compose_mtx_NOD13.i32";
connectAttr "remapValue2.vl[1].vlfv" "xy_axis_NOD13.u";
connectAttr "loftedSurfaceShape2.ws" "xy_axis_NOD13.is";
connectAttr "xy_axis_NOD13.nn" "z_axis_NOD13.i1";
connectAttr "xy_axis_NOD13.ntu" "z_axis_NOD13.i2";
connectAttr "compose_mtx_NOD14.o" "decompose_mtx_NOD14.imat";
connectAttr "xy_axis_NOD14.nnx" "compose_mtx_NOD14.i00";
connectAttr "xy_axis_NOD14.nny" "compose_mtx_NOD14.i01";
connectAttr "xy_axis_NOD14.nnz" "compose_mtx_NOD14.i02";
connectAttr "xy_axis_NOD14.nux" "compose_mtx_NOD14.i10";
connectAttr "xy_axis_NOD14.nuy" "compose_mtx_NOD14.i11";
connectAttr "xy_axis_NOD14.nuz" "compose_mtx_NOD14.i12";
connectAttr "z_axis_NOD14.ox" "compose_mtx_NOD14.i20";
connectAttr "z_axis_NOD14.oy" "compose_mtx_NOD14.i21";
connectAttr "z_axis_NOD14.oz" "compose_mtx_NOD14.i22";
connectAttr "xy_axis_NOD14.px" "compose_mtx_NOD14.i30";
connectAttr "xy_axis_NOD14.py" "compose_mtx_NOD14.i31";
connectAttr "xy_axis_NOD14.pz" "compose_mtx_NOD14.i32";
connectAttr "remapValue2.vl[2].vlfv" "xy_axis_NOD14.u";
connectAttr "loftedSurfaceShape2.ws" "xy_axis_NOD14.is";
connectAttr "xy_axis_NOD14.nn" "z_axis_NOD14.i1";
connectAttr "xy_axis_NOD14.ntu" "z_axis_NOD14.i2";
connectAttr "compose_mtx_NOD15.o" "decompose_mtx_NOD15.imat";
connectAttr "xy_axis_NOD15.nnx" "compose_mtx_NOD15.i00";
connectAttr "xy_axis_NOD15.nny" "compose_mtx_NOD15.i01";
connectAttr "xy_axis_NOD15.nnz" "compose_mtx_NOD15.i02";
connectAttr "xy_axis_NOD15.nux" "compose_mtx_NOD15.i10";
connectAttr "xy_axis_NOD15.nuy" "compose_mtx_NOD15.i11";
connectAttr "xy_axis_NOD15.nuz" "compose_mtx_NOD15.i12";
connectAttr "z_axis_NOD15.ox" "compose_mtx_NOD15.i20";
connectAttr "z_axis_NOD15.oy" "compose_mtx_NOD15.i21";
connectAttr "z_axis_NOD15.oz" "compose_mtx_NOD15.i22";
connectAttr "xy_axis_NOD15.px" "compose_mtx_NOD15.i30";
connectAttr "xy_axis_NOD15.py" "compose_mtx_NOD15.i31";
connectAttr "xy_axis_NOD15.pz" "compose_mtx_NOD15.i32";
connectAttr "remapValue2.vl[3].vlfv" "xy_axis_NOD15.u";
connectAttr "loftedSurfaceShape2.ws" "xy_axis_NOD15.is";
connectAttr "xy_axis_NOD15.nn" "z_axis_NOD15.i1";
connectAttr "xy_axis_NOD15.ntu" "z_axis_NOD15.i2";
connectAttr "compose_mtx_NOD16.o" "decompose_mtx_NOD16.imat";
connectAttr "xy_axis_NOD16.nnx" "compose_mtx_NOD16.i00";
connectAttr "xy_axis_NOD16.nny" "compose_mtx_NOD16.i01";
connectAttr "xy_axis_NOD16.nnz" "compose_mtx_NOD16.i02";
connectAttr "xy_axis_NOD16.nux" "compose_mtx_NOD16.i10";
connectAttr "xy_axis_NOD16.nuy" "compose_mtx_NOD16.i11";
connectAttr "xy_axis_NOD16.nuz" "compose_mtx_NOD16.i12";
connectAttr "z_axis_NOD16.ox" "compose_mtx_NOD16.i20";
connectAttr "z_axis_NOD16.oy" "compose_mtx_NOD16.i21";
connectAttr "z_axis_NOD16.oz" "compose_mtx_NOD16.i22";
connectAttr "xy_axis_NOD16.px" "compose_mtx_NOD16.i30";
connectAttr "xy_axis_NOD16.py" "compose_mtx_NOD16.i31";
connectAttr "xy_axis_NOD16.pz" "compose_mtx_NOD16.i32";
connectAttr "remapValue2.vl[4].vlfv" "xy_axis_NOD16.u";
connectAttr "loftedSurfaceShape2.ws" "xy_axis_NOD16.is";
connectAttr "xy_axis_NOD16.nn" "z_axis_NOD16.i1";
connectAttr "xy_axis_NOD16.ntu" "z_axis_NOD16.i2";
connectAttr "compose_mtx_NOD17.o" "decompose_mtx_NOD17.imat";
connectAttr "xy_axis_NOD17.nnx" "compose_mtx_NOD17.i00";
connectAttr "xy_axis_NOD17.nny" "compose_mtx_NOD17.i01";
connectAttr "xy_axis_NOD17.nnz" "compose_mtx_NOD17.i02";
connectAttr "xy_axis_NOD17.nux" "compose_mtx_NOD17.i10";
connectAttr "xy_axis_NOD17.nuy" "compose_mtx_NOD17.i11";
connectAttr "xy_axis_NOD17.nuz" "compose_mtx_NOD17.i12";
connectAttr "z_axis_NOD17.ox" "compose_mtx_NOD17.i20";
connectAttr "z_axis_NOD17.oy" "compose_mtx_NOD17.i21";
connectAttr "z_axis_NOD17.oz" "compose_mtx_NOD17.i22";
connectAttr "xy_axis_NOD17.px" "compose_mtx_NOD17.i30";
connectAttr "xy_axis_NOD17.py" "compose_mtx_NOD17.i31";
connectAttr "xy_axis_NOD17.pz" "compose_mtx_NOD17.i32";
connectAttr "remapValue2.vl[5].vlfv" "xy_axis_NOD17.u";
connectAttr "loftedSurfaceShape2.ws" "xy_axis_NOD17.is";
connectAttr "xy_axis_NOD17.nn" "z_axis_NOD17.i1";
connectAttr "xy_axis_NOD17.ntu" "z_axis_NOD17.i2";
connectAttr "compose_mtx_NOD18.o" "decompose_mtx_NOD18.imat";
connectAttr "xy_axis_NOD18.nnx" "compose_mtx_NOD18.i00";
connectAttr "xy_axis_NOD18.nny" "compose_mtx_NOD18.i01";
connectAttr "xy_axis_NOD18.nnz" "compose_mtx_NOD18.i02";
connectAttr "xy_axis_NOD18.nux" "compose_mtx_NOD18.i10";
connectAttr "xy_axis_NOD18.nuy" "compose_mtx_NOD18.i11";
connectAttr "xy_axis_NOD18.nuz" "compose_mtx_NOD18.i12";
connectAttr "z_axis_NOD18.ox" "compose_mtx_NOD18.i20";
connectAttr "z_axis_NOD18.oy" "compose_mtx_NOD18.i21";
connectAttr "z_axis_NOD18.oz" "compose_mtx_NOD18.i22";
connectAttr "xy_axis_NOD18.px" "compose_mtx_NOD18.i30";
connectAttr "xy_axis_NOD18.py" "compose_mtx_NOD18.i31";
connectAttr "xy_axis_NOD18.pz" "compose_mtx_NOD18.i32";
connectAttr "remapValue2.vl[6].vlfv" "xy_axis_NOD18.u";
connectAttr "loftedSurfaceShape2.ws" "xy_axis_NOD18.is";
connectAttr "xy_axis_NOD18.nn" "z_axis_NOD18.i1";
connectAttr "xy_axis_NOD18.ntu" "z_axis_NOD18.i2";
connectAttr "compose_mtx_NOD19.o" "decompose_mtx_NOD19.imat";
connectAttr "xy_axis_NOD19.nnx" "compose_mtx_NOD19.i00";
connectAttr "xy_axis_NOD19.nny" "compose_mtx_NOD19.i01";
connectAttr "xy_axis_NOD19.nnz" "compose_mtx_NOD19.i02";
connectAttr "xy_axis_NOD19.nux" "compose_mtx_NOD19.i10";
connectAttr "xy_axis_NOD19.nuy" "compose_mtx_NOD19.i11";
connectAttr "xy_axis_NOD19.nuz" "compose_mtx_NOD19.i12";
connectAttr "z_axis_NOD19.ox" "compose_mtx_NOD19.i20";
connectAttr "z_axis_NOD19.oy" "compose_mtx_NOD19.i21";
connectAttr "z_axis_NOD19.oz" "compose_mtx_NOD19.i22";
connectAttr "xy_axis_NOD19.px" "compose_mtx_NOD19.i30";
connectAttr "xy_axis_NOD19.py" "compose_mtx_NOD19.i31";
connectAttr "xy_axis_NOD19.pz" "compose_mtx_NOD19.i32";
connectAttr "remapValue2.vl[7].vlfv" "xy_axis_NOD19.u";
connectAttr "loftedSurfaceShape2.ws" "xy_axis_NOD19.is";
connectAttr "xy_axis_NOD19.nn" "z_axis_NOD19.i1";
connectAttr "xy_axis_NOD19.ntu" "z_axis_NOD19.i2";
connectAttr "compose_mtx_NOD20.o" "decompose_mtx_NOD20.imat";
connectAttr "xy_axis_NOD20.nnx" "compose_mtx_NOD20.i00";
connectAttr "xy_axis_NOD20.nny" "compose_mtx_NOD20.i01";
connectAttr "xy_axis_NOD20.nnz" "compose_mtx_NOD20.i02";
connectAttr "xy_axis_NOD20.nux" "compose_mtx_NOD20.i10";
connectAttr "xy_axis_NOD20.nuy" "compose_mtx_NOD20.i11";
connectAttr "xy_axis_NOD20.nuz" "compose_mtx_NOD20.i12";
connectAttr "z_axis_NOD20.ox" "compose_mtx_NOD20.i20";
connectAttr "z_axis_NOD20.oy" "compose_mtx_NOD20.i21";
connectAttr "z_axis_NOD20.oz" "compose_mtx_NOD20.i22";
connectAttr "xy_axis_NOD20.px" "compose_mtx_NOD20.i30";
connectAttr "xy_axis_NOD20.py" "compose_mtx_NOD20.i31";
connectAttr "xy_axis_NOD20.pz" "compose_mtx_NOD20.i32";
connectAttr "remapValue2.vl[8].vlfv" "xy_axis_NOD20.u";
connectAttr "loftedSurfaceShape2.ws" "xy_axis_NOD20.is";
connectAttr "xy_axis_NOD20.nn" "z_axis_NOD20.i1";
connectAttr "xy_axis_NOD20.ntu" "z_axis_NOD20.i2";
connectAttr "compose_mtx_NOD21.o" "decompose_mtx_NOD21.imat";
connectAttr "xy_axis_NOD21.nnx" "compose_mtx_NOD21.i00";
connectAttr "xy_axis_NOD21.nny" "compose_mtx_NOD21.i01";
connectAttr "xy_axis_NOD21.nnz" "compose_mtx_NOD21.i02";
connectAttr "xy_axis_NOD21.nux" "compose_mtx_NOD21.i10";
connectAttr "xy_axis_NOD21.nuy" "compose_mtx_NOD21.i11";
connectAttr "xy_axis_NOD21.nuz" "compose_mtx_NOD21.i12";
connectAttr "z_axis_NOD21.ox" "compose_mtx_NOD21.i20";
connectAttr "z_axis_NOD21.oy" "compose_mtx_NOD21.i21";
connectAttr "z_axis_NOD21.oz" "compose_mtx_NOD21.i22";
connectAttr "xy_axis_NOD21.px" "compose_mtx_NOD21.i30";
connectAttr "xy_axis_NOD21.py" "compose_mtx_NOD21.i31";
connectAttr "xy_axis_NOD21.pz" "compose_mtx_NOD21.i32";
connectAttr "remapValue2.vl[9].vlfv" "xy_axis_NOD21.u";
connectAttr "loftedSurfaceShape2.ws" "xy_axis_NOD21.is";
connectAttr "xy_axis_NOD21.nn" "z_axis_NOD21.i1";
connectAttr "xy_axis_NOD21.ntu" "z_axis_NOD21.i2";
connectAttr "test_slide_shift_clamp2.opr" "test_slide_shift_mdl2.i2";
connectAttr "test_slide_shift_ctrl_clamp.opr" "test_slide_shift_ctrl_mdl.i2";
connectAttr "bezier_CON.wm" "test_a_line_001_dm_002.imat";
connectAttr "bezierHandleA_CON.wm" "test_a_line_001_dm_001.imat";
connectAttr "bezierHandleB_CON.wm" "test_b_line_000_dm_003.imat";
connectAttr "bezier_CON.wm" "test_a_line_000_dm_002.imat";
connectAttr "polyCylinder1.out" "transformGeometry1.ig";
connectAttr "skinCluster3GroupParts.og" "skinCluster3.ip[0].ig";
connectAttr "skinCluster3GroupId.id" "skinCluster3.ip[0].gi";
connectAttr "bindPose3.msg" "skinCluster3.bp";
connectAttr "|cartoony_GRP|upper_GRP|rivet1_OFS|seg1_JNT.wm" "skinCluster3.ma[0]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet2_OFS|seg2_JNT.wm" "skinCluster3.ma[1]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet3_OFS|seg3_JNT.wm" "skinCluster3.ma[2]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet4_OFS|seg4_JNT.wm" "skinCluster3.ma[3]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet5_OFS|seg5_JNT.wm" "skinCluster3.ma[4]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet6_OFS|seg6_JNT.wm" "skinCluster3.ma[5]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet7_OFS|seg7_JNT.wm" "skinCluster3.ma[6]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet8_OFS|seg8_JNT.wm" "skinCluster3.ma[7]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet9_OFS|seg9_JNT.wm" "skinCluster3.ma[8]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet10_OFS|seg10_JNT.wm" "skinCluster3.ma[9]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet1_OFS|seg1_JNT.wm" "skinCluster3.ma[10]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet2_OFS|seg2_JNT.wm" "skinCluster3.ma[11]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet3_OFS|seg3_JNT.wm" "skinCluster3.ma[12]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet4_OFS|seg4_JNT.wm" "skinCluster3.ma[13]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet5_OFS|seg5_JNT.wm" "skinCluster3.ma[14]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet6_OFS|seg6_JNT.wm" "skinCluster3.ma[15]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet7_OFS|seg7_JNT.wm" "skinCluster3.ma[16]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet8_OFS|seg8_JNT.wm" "skinCluster3.ma[17]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet9_OFS|seg9_JNT.wm" "skinCluster3.ma[18]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet10_OFS|seg10_JNT.wm" "skinCluster3.ma[19]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet1_OFS|seg1_JNT.liw" "skinCluster3.lw[0]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet2_OFS|seg2_JNT.liw" "skinCluster3.lw[1]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet3_OFS|seg3_JNT.liw" "skinCluster3.lw[2]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet4_OFS|seg4_JNT.liw" "skinCluster3.lw[3]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet5_OFS|seg5_JNT.liw" "skinCluster3.lw[4]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet6_OFS|seg6_JNT.liw" "skinCluster3.lw[5]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet7_OFS|seg7_JNT.liw" "skinCluster3.lw[6]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet8_OFS|seg8_JNT.liw" "skinCluster3.lw[7]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet9_OFS|seg9_JNT.liw" "skinCluster3.lw[8]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet10_OFS|seg10_JNT.liw" "skinCluster3.lw[9]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet1_OFS|seg1_JNT.liw" "skinCluster3.lw[10]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet2_OFS|seg2_JNT.liw" "skinCluster3.lw[11]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet3_OFS|seg3_JNT.liw" "skinCluster3.lw[12]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet4_OFS|seg4_JNT.liw" "skinCluster3.lw[13]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet5_OFS|seg5_JNT.liw" "skinCluster3.lw[14]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet6_OFS|seg6_JNT.liw" "skinCluster3.lw[15]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet7_OFS|seg7_JNT.liw" "skinCluster3.lw[16]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet8_OFS|seg8_JNT.liw" "skinCluster3.lw[17]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet9_OFS|seg9_JNT.liw" "skinCluster3.lw[18]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet10_OFS|seg10_JNT.liw" "skinCluster3.lw[19]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet1_OFS|seg1_JNT.obcc" "skinCluster3.ifcl[0]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet2_OFS|seg2_JNT.obcc" "skinCluster3.ifcl[1]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet3_OFS|seg3_JNT.obcc" "skinCluster3.ifcl[2]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet4_OFS|seg4_JNT.obcc" "skinCluster3.ifcl[3]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet5_OFS|seg5_JNT.obcc" "skinCluster3.ifcl[4]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet6_OFS|seg6_JNT.obcc" "skinCluster3.ifcl[5]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet7_OFS|seg7_JNT.obcc" "skinCluster3.ifcl[6]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet8_OFS|seg8_JNT.obcc" "skinCluster3.ifcl[7]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet9_OFS|seg9_JNT.obcc" "skinCluster3.ifcl[8]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet10_OFS|seg10_JNT.obcc" "skinCluster3.ifcl[9]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet1_OFS|seg1_JNT.obcc" "skinCluster3.ifcl[10]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet2_OFS|seg2_JNT.obcc" "skinCluster3.ifcl[11]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet3_OFS|seg3_JNT.obcc" "skinCluster3.ifcl[12]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet4_OFS|seg4_JNT.obcc" "skinCluster3.ifcl[13]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet5_OFS|seg5_JNT.obcc" "skinCluster3.ifcl[14]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet6_OFS|seg6_JNT.obcc" "skinCluster3.ifcl[15]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet7_OFS|seg7_JNT.obcc" "skinCluster3.ifcl[16]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet8_OFS|seg8_JNT.obcc" "skinCluster3.ifcl[17]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet9_OFS|seg9_JNT.obcc" "skinCluster3.ifcl[18]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet10_OFS|seg10_JNT.obcc" "skinCluster3.ifcl[19]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet3_OFS|seg3_JNT.msg" "skinCluster3.ptt"
		;
connectAttr "groupParts24.og" "tweak6.ip[0].ig";
connectAttr "groupId27.id" "tweak6.ip[0].gi";
connectAttr "skinCluster3GroupId.msg" "skinCluster3Set.gn" -na;
connectAttr "pCylinderShape1.iog.og[0]" "skinCluster3Set.dsm" -na;
connectAttr "skinCluster3.msg" "skinCluster3Set.ub[0]";
connectAttr "tweak6.og[0]" "skinCluster3GroupParts.ig";
connectAttr "skinCluster3GroupId.id" "skinCluster3GroupParts.gi";
connectAttr "groupId27.msg" "tweakSet6.gn" -na;
connectAttr "pCylinderShape1.iog.og[1]" "tweakSet6.dsm" -na;
connectAttr "tweak6.msg" "tweakSet6.ub[0]";
connectAttr "pCylinderShape1Orig.w" "groupParts24.ig";
connectAttr "groupId27.id" "groupParts24.gi";
connectAttr "cartoony_GRP.msg" "bindPose3.m[0]";
connectAttr "upper_GRP.msg" "bindPose3.m[1]";
connectAttr "|cartoony_GRP|upper_GRP|rivet1_OFS.msg" "bindPose3.m[2]";
connectAttr "|cartoony_GRP|upper_GRP|rivet1_OFS|seg1_JNT.msg" "bindPose3.m[3]";
connectAttr "|cartoony_GRP|upper_GRP|rivet2_OFS.msg" "bindPose3.m[4]";
connectAttr "|cartoony_GRP|upper_GRP|rivet2_OFS|seg2_JNT.msg" "bindPose3.m[5]";
connectAttr "|cartoony_GRP|upper_GRP|rivet3_OFS.msg" "bindPose3.m[6]";
connectAttr "|cartoony_GRP|upper_GRP|rivet3_OFS|seg3_JNT.msg" "bindPose3.m[7]";
connectAttr "|cartoony_GRP|upper_GRP|rivet4_OFS.msg" "bindPose3.m[8]";
connectAttr "|cartoony_GRP|upper_GRP|rivet4_OFS|seg4_JNT.msg" "bindPose3.m[9]";
connectAttr "|cartoony_GRP|upper_GRP|rivet5_OFS.msg" "bindPose3.m[10]";
connectAttr "|cartoony_GRP|upper_GRP|rivet5_OFS|seg5_JNT.msg" "bindPose3.m[11]";
connectAttr "|cartoony_GRP|upper_GRP|rivet6_OFS.msg" "bindPose3.m[12]";
connectAttr "|cartoony_GRP|upper_GRP|rivet6_OFS|seg6_JNT.msg" "bindPose3.m[13]";
connectAttr "|cartoony_GRP|upper_GRP|rivet7_OFS.msg" "bindPose3.m[14]";
connectAttr "|cartoony_GRP|upper_GRP|rivet7_OFS|seg7_JNT.msg" "bindPose3.m[15]";
connectAttr "|cartoony_GRP|upper_GRP|rivet8_OFS.msg" "bindPose3.m[16]";
connectAttr "|cartoony_GRP|upper_GRP|rivet8_OFS|seg8_JNT.msg" "bindPose3.m[17]";
connectAttr "|cartoony_GRP|upper_GRP|rivet9_OFS.msg" "bindPose3.m[18]";
connectAttr "|cartoony_GRP|upper_GRP|rivet9_OFS|seg9_JNT.msg" "bindPose3.m[19]";
connectAttr "|cartoony_GRP|upper_GRP|rivet10_OFS.msg" "bindPose3.m[20]";
connectAttr "|cartoony_GRP|upper_GRP|rivet10_OFS|seg10_JNT.msg" "bindPose3.m[21]"
		;
connectAttr "lower_GRP.msg" "bindPose3.m[22]";
connectAttr "|cartoony_GRP|lower_GRP|rivet1_OFS.msg" "bindPose3.m[23]";
connectAttr "|cartoony_GRP|lower_GRP|rivet1_OFS|seg1_JNT.msg" "bindPose3.m[24]";
connectAttr "|cartoony_GRP|lower_GRP|rivet2_OFS.msg" "bindPose3.m[25]";
connectAttr "|cartoony_GRP|lower_GRP|rivet2_OFS|seg2_JNT.msg" "bindPose3.m[26]";
connectAttr "|cartoony_GRP|lower_GRP|rivet3_OFS.msg" "bindPose3.m[27]";
connectAttr "|cartoony_GRP|lower_GRP|rivet3_OFS|seg3_JNT.msg" "bindPose3.m[28]";
connectAttr "|cartoony_GRP|lower_GRP|rivet4_OFS.msg" "bindPose3.m[29]";
connectAttr "|cartoony_GRP|lower_GRP|rivet4_OFS|seg4_JNT.msg" "bindPose3.m[30]";
connectAttr "|cartoony_GRP|lower_GRP|rivet5_OFS.msg" "bindPose3.m[31]";
connectAttr "|cartoony_GRP|lower_GRP|rivet5_OFS|seg5_JNT.msg" "bindPose3.m[32]";
connectAttr "|cartoony_GRP|lower_GRP|rivet6_OFS.msg" "bindPose3.m[33]";
connectAttr "|cartoony_GRP|lower_GRP|rivet6_OFS|seg6_JNT.msg" "bindPose3.m[34]";
connectAttr "|cartoony_GRP|lower_GRP|rivet7_OFS.msg" "bindPose3.m[35]";
connectAttr "|cartoony_GRP|lower_GRP|rivet7_OFS|seg7_JNT.msg" "bindPose3.m[36]";
connectAttr "|cartoony_GRP|lower_GRP|rivet8_OFS.msg" "bindPose3.m[37]";
connectAttr "|cartoony_GRP|lower_GRP|rivet8_OFS|seg8_JNT.msg" "bindPose3.m[38]";
connectAttr "|cartoony_GRP|lower_GRP|rivet9_OFS.msg" "bindPose3.m[39]";
connectAttr "|cartoony_GRP|lower_GRP|rivet9_OFS|seg9_JNT.msg" "bindPose3.m[40]";
connectAttr "|cartoony_GRP|lower_GRP|rivet10_OFS.msg" "bindPose3.m[41]";
connectAttr "|cartoony_GRP|lower_GRP|rivet10_OFS|seg10_JNT.msg" "bindPose3.m[42]"
		;
connectAttr "bindPose3.w" "bindPose3.p[0]";
connectAttr "bindPose3.m[0]" "bindPose3.p[1]";
connectAttr "bindPose3.m[1]" "bindPose3.p[2]";
connectAttr "bindPose3.m[2]" "bindPose3.p[3]";
connectAttr "bindPose3.m[1]" "bindPose3.p[4]";
connectAttr "bindPose3.m[4]" "bindPose3.p[5]";
connectAttr "bindPose3.m[1]" "bindPose3.p[6]";
connectAttr "bindPose3.m[6]" "bindPose3.p[7]";
connectAttr "bindPose3.m[1]" "bindPose3.p[8]";
connectAttr "bindPose3.m[8]" "bindPose3.p[9]";
connectAttr "bindPose3.m[1]" "bindPose3.p[10]";
connectAttr "bindPose3.m[10]" "bindPose3.p[11]";
connectAttr "bindPose3.m[1]" "bindPose3.p[12]";
connectAttr "bindPose3.m[12]" "bindPose3.p[13]";
connectAttr "bindPose3.m[1]" "bindPose3.p[14]";
connectAttr "bindPose3.m[14]" "bindPose3.p[15]";
connectAttr "bindPose3.m[1]" "bindPose3.p[16]";
connectAttr "bindPose3.m[16]" "bindPose3.p[17]";
connectAttr "bindPose3.m[1]" "bindPose3.p[18]";
connectAttr "bindPose3.m[18]" "bindPose3.p[19]";
connectAttr "bindPose3.m[1]" "bindPose3.p[20]";
connectAttr "bindPose3.m[20]" "bindPose3.p[21]";
connectAttr "bindPose3.m[0]" "bindPose3.p[22]";
connectAttr "bindPose3.m[22]" "bindPose3.p[23]";
connectAttr "bindPose3.m[23]" "bindPose3.p[24]";
connectAttr "bindPose3.m[22]" "bindPose3.p[25]";
connectAttr "bindPose3.m[25]" "bindPose3.p[26]";
connectAttr "bindPose3.m[22]" "bindPose3.p[27]";
connectAttr "bindPose3.m[27]" "bindPose3.p[28]";
connectAttr "bindPose3.m[22]" "bindPose3.p[29]";
connectAttr "bindPose3.m[29]" "bindPose3.p[30]";
connectAttr "bindPose3.m[22]" "bindPose3.p[31]";
connectAttr "bindPose3.m[31]" "bindPose3.p[32]";
connectAttr "bindPose3.m[22]" "bindPose3.p[33]";
connectAttr "bindPose3.m[33]" "bindPose3.p[34]";
connectAttr "bindPose3.m[22]" "bindPose3.p[35]";
connectAttr "bindPose3.m[35]" "bindPose3.p[36]";
connectAttr "bindPose3.m[22]" "bindPose3.p[37]";
connectAttr "bindPose3.m[37]" "bindPose3.p[38]";
connectAttr "bindPose3.m[22]" "bindPose3.p[39]";
connectAttr "bindPose3.m[39]" "bindPose3.p[40]";
connectAttr "bindPose3.m[22]" "bindPose3.p[41]";
connectAttr "bindPose3.m[41]" "bindPose3.p[42]";
connectAttr "|cartoony_GRP|upper_GRP|rivet1_OFS|seg1_JNT.bps" "bindPose3.wm[3]";
connectAttr "|cartoony_GRP|upper_GRP|rivet2_OFS|seg2_JNT.bps" "bindPose3.wm[5]";
connectAttr "|cartoony_GRP|upper_GRP|rivet3_OFS|seg3_JNT.bps" "bindPose3.wm[7]";
connectAttr "|cartoony_GRP|upper_GRP|rivet4_OFS|seg4_JNT.bps" "bindPose3.wm[9]";
connectAttr "|cartoony_GRP|upper_GRP|rivet5_OFS|seg5_JNT.bps" "bindPose3.wm[11]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet6_OFS|seg6_JNT.bps" "bindPose3.wm[13]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet7_OFS|seg7_JNT.bps" "bindPose3.wm[15]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet8_OFS|seg8_JNT.bps" "bindPose3.wm[17]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet9_OFS|seg9_JNT.bps" "bindPose3.wm[19]"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet10_OFS|seg10_JNT.bps" "bindPose3.wm[21]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet1_OFS|seg1_JNT.bps" "bindPose3.wm[24]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet2_OFS|seg2_JNT.bps" "bindPose3.wm[26]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet3_OFS|seg3_JNT.bps" "bindPose3.wm[28]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet4_OFS|seg4_JNT.bps" "bindPose3.wm[30]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet5_OFS|seg5_JNT.bps" "bindPose3.wm[32]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet6_OFS|seg6_JNT.bps" "bindPose3.wm[34]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet7_OFS|seg7_JNT.bps" "bindPose3.wm[36]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet8_OFS|seg8_JNT.bps" "bindPose3.wm[38]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet9_OFS|seg9_JNT.bps" "bindPose3.wm[40]"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet10_OFS|seg10_JNT.bps" "bindPose3.wm[42]"
		;
connectAttr "makeNurbPlane2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[0].dn";
connectAttr "xy_axis_NOD13.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[1].dn";
connectAttr "nurbsPlaneShape2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[2].dn"
		;
connectAttr "compose_mtx_NOD3.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[3].dn"
		;
connectAttr "xy_axis_NOD4.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[4].dn";
connectAttr "lower_start.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[5].dn";
connectAttr "|cartoony_GRP|lower_GRP|rivet8_OFS.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[6].dn"
		;
connectAttr "xy_axis_NOD10.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[7].dn";
connectAttr "decompose_mtx_NOD17.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[8].dn"
		;
connectAttr "loftedSurfaceShape1.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[9].dn"
		;
connectAttr "z_axis_NOD6.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[10].dn";
connectAttr "xy_axis_NOD11.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[11].dn";
connectAttr "xy_axis_NOD2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[12].dn";
connectAttr "compose_mtx_NOD9.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[13].dn"
		;
connectAttr "ffd1Base1.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[14].dn";
connectAttr "|cartoony_GRP|lower_GRP|rivet9_OFS.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[15].dn"
		;
connectAttr "bindPose2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[16].dn";
connectAttr "xy_axis_NOD6.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[17].dn";
connectAttr "|cartoony_GRP|upper_GRP|rivet1_OFS.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[18].dn"
		;
connectAttr "ffd2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[19].dn";
connectAttr "duplicatedCurve5.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[20].dn"
		;
connectAttr "decompose_mtx_NOD5.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[21].dn"
		;
connectAttr "xy_axis_NOD3.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[22].dn";
connectAttr "compose_mtx_NOD4.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[23].dn"
		;
connectAttr "duplicatedCurveShape4.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[24].dn"
		;
connectAttr "z_axis_NOD2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[25].dn";
connectAttr "z_axis_NOD16.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[26].dn";
connectAttr "decompose_mtx_NOD19.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[27].dn"
		;
connectAttr "curveFromSurfaceIso4.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[28].dn"
		;
connectAttr "ffd1Lattice1.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[29].dn";
connectAttr "|cartoony_GRP|upper_GRP|rivet3_OFS.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[30].dn"
		;
connectAttr "z_axis_NOD7.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[31].dn";
connectAttr "ffd1Set1.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[32].dn";
connectAttr "compose_mtx_NOD17.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[33].dn"
		;
connectAttr "z_axis_NOD21.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[34].dn";
connectAttr "|cartoony_GRP|upper_GRP|rivet6_OFS.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[35].dn"
		;
connectAttr "duplicatedCurve4.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[36].dn"
		;
connectAttr "compose_mtx_NOD12.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[37].dn"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet3_OFS.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[38].dn"
		;
connectAttr "decompose_mtx_NOD7.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[39].dn"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet10_OFS.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[40].dn"
		;
connectAttr "decompose_mtx_NOD18.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[41].dn"
		;
connectAttr "curveFromSurfaceIso3.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[42].dn"
		;
connectAttr "compose_mtx_NOD18.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[43].dn"
		;
connectAttr "compose_mtx_NOD19.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[44].dn"
		;
connectAttr "tweakSet5.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[45].dn";
connectAttr "compose_mtx_NOD14.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[46].dn"
		;
connectAttr "xy_axis_NOD18.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[47].dn";
connectAttr "compose_mtx_NOD11.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[48].dn"
		;
connectAttr "skinCluster1Set1.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[49].dn"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet5_OFS|seg5_JNT.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[50].dn"
		;
connectAttr "compose_mtx_NOD20.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[51].dn"
		;
connectAttr "compose_mtx_NOD16.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[52].dn"
		;
connectAttr "lower_end.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[53].dn";
connectAttr "compose_mtx_NOD21.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[54].dn"
		;
connectAttr "loftedSurfaceShape2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[55].dn"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet7_OFS.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[56].dn"
		;
connectAttr "z_axis_NOD19.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[57].dn";
connectAttr "decompose_mtx_NOD15.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[58].dn"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet10_OFS|seg10_JNT.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[59].dn"
		;
connectAttr "z_axis_NOD12.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[60].dn";
connectAttr "|cartoony_GRP|lower_GRP|rivet3_OFS|seg3_JNT.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[61].dn"
		;
connectAttr "loftedSurface2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[62].dn"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet8_OFS|seg8_JNT.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[63].dn"
		;
connectAttr "z_axis_NOD15.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[64].dn";
connectAttr "rebuildCurve3.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[65].dn";
connectAttr "lower_mid.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[66].dn";
connectAttr "ffd1Lattice1Shape.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[67].dn"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet1_OFS|seg1_JNT.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[68].dn"
		;
connectAttr "z_axis_NOD17.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[69].dn";
connectAttr "compose_mtx_NOD6.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[70].dn"
		;
connectAttr "tweak4.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[71].dn";
connectAttr "xy_axis_NOD16.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[72].dn";
connectAttr "ffd1Base1Shape.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[73].dn"
		;
connectAttr "decompose_mtx_NOD4.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[74].dn"
		;
connectAttr "z_axis_NOD9.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[75].dn";
connectAttr "remapValue2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[76].dn";
connectAttr "xy_axis_NOD17.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[77].dn";
connectAttr "compose_mtx_NOD13.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[78].dn"
		;
connectAttr "decompose_mtx_NOD21.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[79].dn"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet4_OFS|seg4_JNT.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[80].dn"
		;
connectAttr "lower_GRP.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[81].dn";
connectAttr "compose_mtx_NOD2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[82].dn"
		;
connectAttr "z_axis_NOD20.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[83].dn";
connectAttr "|cartoony_GRP|lower_GRP|rivet7_OFS|seg7_JNT.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[84].dn"
		;
connectAttr "decompose_mtx_NOD6.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[85].dn"
		;
connectAttr "loft2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[86].dn";
connectAttr "skinCluster2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[87].dn";
connectAttr "nurbsPlane2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[88].dn";
connectAttr "decompose_mtx_NOD14.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[89].dn"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet2_OFS.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[90].dn"
		;
connectAttr "decompose_mtx_NOD12.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[91].dn"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet2_OFS.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[92].dn"
		;
connectAttr "z_axis_NOD14.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[93].dn";
connectAttr "compose_mtx_NOD5.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[94].dn"
		;
connectAttr "xy_axis_NOD5.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[95].dn";
connectAttr "compose_mtx_NOD7.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[96].dn"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet2_OFS|seg2_JNT.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[97].dn"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet5_OFS.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[98].dn"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet10_OFS.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[99].dn"
		;
connectAttr "rebuildCurve4.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[100].dn"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet6_OFS.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[101].dn"
		;
connectAttr "z_axis_NOD10.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[102].dn";
connectAttr "compose_mtx_NOD10.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[103].dn"
		;
connectAttr "xy_axis_NOD20.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[104].dn"
		;
connectAttr "xy_axis_NOD21.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[105].dn"
		;
connectAttr "xy_axis_NOD9.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[106].dn";
connectAttr "decompose_mtx_NOD13.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[107].dn"
		;
connectAttr "z_axis_NOD13.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[108].dn";
connectAttr "ffd1Lattice1ShapeOrig.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[109].dn"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet9_OFS.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[110].dn"
		;
connectAttr "z_axis_NOD5.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[111].dn";
connectAttr "rebuildSurface2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[112].dn"
		;
connectAttr "decompose_mtx_NOD8.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[113].dn"
		;
connectAttr "compose_mtx_NOD15.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[114].dn"
		;
connectAttr "z_axis_NOD3.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[115].dn";
connectAttr "|cartoony_GRP|upper_GRP|rivet4_OFS.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[116].dn"
		;
connectAttr "xy_axis_NOD12.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[117].dn"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet1_OFS.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[118].dn"
		;
connectAttr "xy_axis_NOD7.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[119].dn";
connectAttr "duplicatedCurveShape5.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[120].dn"
		;
connectAttr "nurbsPlaneShape1Orig2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[121].dn"
		;
connectAttr "decompose_mtx_NOD2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[122].dn"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet4_OFS.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[123].dn"
		;
connectAttr "upper_GRP.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[124].dn";
connectAttr "decompose_mtx_NOD3.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[125].dn"
		;
connectAttr "decompose_mtx_NOD20.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[126].dn"
		;
connectAttr "remapValue1.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[127].dn";
connectAttr "z_axis_NOD8.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[128].dn";
connectAttr "xy_axis_NOD14.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[129].dn"
		;
connectAttr "z_axis_NOD18.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[130].dn";
connectAttr "decompose_mtx_NOD16.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[131].dn"
		;
connectAttr "xy_axis_NOD19.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[132].dn"
		;
connectAttr "z_axis_NOD4.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[133].dn";
connectAttr "xy_axis_NOD15.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[134].dn"
		;
connectAttr "decompose_mtx_NOD11.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[135].dn"
		;
connectAttr "z_axis_NOD11.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[136].dn";
connectAttr "|cartoony_GRP|lower_GRP|rivet6_OFS|seg6_JNT.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[137].dn"
		;
connectAttr "decompose_mtx_NOD10.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[138].dn"
		;
connectAttr "|cartoony_GRP|upper_GRP|rivet8_OFS.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[139].dn"
		;
connectAttr "tweak5.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[140].dn";
connectAttr "|cartoony_GRP|upper_GRP|rivet7_OFS.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[141].dn"
		;
connectAttr "xy_axis_NOD8.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[142].dn";
connectAttr "|cartoony_GRP|lower_GRP|rivet5_OFS.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[143].dn"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet9_OFS|seg9_JNT.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[144].dn"
		;
connectAttr "decompose_mtx_NOD9.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[145].dn"
		;
connectAttr "compose_mtx_NOD8.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[146].dn"
		;
connectAttr "tweakSet4.msg" "MayaNodeEditorSavedTabsInfo1.tgi[0].ni[147].dn";
connectAttr "slide_RMP1.msg" "MayaNodeEditorSavedTabsInfo1.tgi[1].ni[0].dn";
connectAttr "controls.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[0].dn";
connectAttr "a_line.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[1].dn";
connectAttr "bindPose3.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[2].dn";
connectAttr "transformGeometry1.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[3].dn"
		;
connectAttr "polyCylinder1.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[4].dn";
connectAttr "tweakSet6.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[5].dn";
connectAttr "pCylinderShape1Orig.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[6].dn"
		;
connectAttr "bezier_CON.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[7].dn";
connectAttr "test_a_line_000_dm_002.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[8].dn"
		;
connectAttr "test_a_line_001_dm_002.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[9].dn"
		;
connectAttr "b_line.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[10].dn";
connectAttr "b_line0Shape.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[11].dn";
connectAttr "pCylinder1.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[12].dn";
connectAttr "tweak6.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[13].dn";
connectAttr "test_b_line_000_dm_003.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[14].dn"
		;
connectAttr "skinCluster3Set.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[15].dn"
		;
connectAttr "a_lineShape.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[16].dn";
connectAttr "skinCluster3.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[17].dn";
connectAttr "pCylinderShape1.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[18].dn"
		;
connectAttr "bezierHandleA_CON.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[19].dn"
		;
connectAttr "test_a_line_001_dm_001.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[20].dn"
		;
connectAttr "bezierHandleB_CON.msg" "MayaNodeEditorSavedTabsInfo1.tgi[2].ni[21].dn"
		;
connectAttr "xy_axis_NOD12.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[0].dn";
connectAttr "duplicatedCurveShape4.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[1].dn"
		;
connectAttr "ffd1Lattice1ShapeOrig.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[2].dn"
		;
connectAttr "ffd2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[3].dn";
connectAttr "ffd1Base1Shape.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[4].dn";
connectAttr "curveFromSurfaceIso3.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[5].dn"
		;
connectAttr "rebuildCurve3.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[6].dn";
connectAttr "upper_end_parentConstraint1.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[7].dn"
		;
connectAttr "|cartoony_GRP|lower_GRP|rivet1_OFS.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[8].dn"
		;
connectAttr "nurbsPlaneShape1Orig2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[9].dn"
		;
connectAttr "lower_mid_parentConstraint1.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[10].dn"
		;
connectAttr "compose_mtx_NOD12.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[11].dn"
		;
connectAttr "rebuildCurve4.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[12].dn";
connectAttr "upper_start_parentConstraint1.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[13].dn"
		;
connectAttr "lower_end_parentConstraint1.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[14].dn"
		;
connectAttr "bindPose3.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[15].dn";
connectAttr "ffd1Lattice1Shape.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[16].dn"
		;
connectAttr "duplicatedCurveShape5.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[17].dn"
		;
connectAttr "tweak4.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[18].dn";
connectAttr "loft2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[19].dn";
connectAttr "lower_start_parentConstraint1.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[20].dn"
		;
connectAttr "rebuildSurface2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[21].dn"
		;
connectAttr "upper_mid_parentConstraint1.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[22].dn"
		;
connectAttr "lower_end.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[23].dn";
connectAttr "nurbsPlaneShape2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[24].dn"
		;
connectAttr "z_axis_NOD12.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[25].dn";
connectAttr "skinCluster2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[26].dn";
connectAttr "lower_mid.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[27].dn";
connectAttr "decompose_mtx_NOD12.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[28].dn"
		;
connectAttr "makeNurbPlane2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[29].dn"
		;
connectAttr "loftedSurfaceShape2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[30].dn"
		;
connectAttr "curveFromSurfaceIso4.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[31].dn"
		;
connectAttr "remapValue2.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[32].dn";
connectAttr "lower_start.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[33].dn";
connectAttr "tweak5.msg" "MayaNodeEditorSavedTabsInfo1.tgi[5].ni[34].dn";
connectAttr "lambert2SG.pa" ":renderPartition.st" -na;
connectAttr "lambert3SG.pa" ":renderPartition.st" -na;
connectAttr "lambert4SG.pa" ":renderPartition.st" -na;
connectAttr "lambert2.msg" ":defaultShaderList1.s" -na;
connectAttr "lambert3.msg" ":defaultShaderList1.s" -na;
connectAttr "lambert4.msg" ":defaultShaderList1.s" -na;
connectAttr "slide_RMP1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "slide_RMP2.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "remapValue1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "remapValue2.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "nurbsPlaneShape1.iog" ":initialShadingGroup.dsm" -na;
connectAttr "loftedSurfaceShape1.iog" ":initialShadingGroup.dsm" -na;
connectAttr "nurbsPlaneShape2.iog" ":initialShadingGroup.dsm" -na;
connectAttr "loftedSurfaceShape2.iog" ":initialShadingGroup.dsm" -na;
connectAttr "pCylinderShape1.iog" ":initialShadingGroup.dsm" -na;
connectAttr "ikSCsolver.msg" ":ikSystem.sol" -na;
// End of result.ma
