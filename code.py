$begin 'AnsoftProject' Created='Fri Dec 17 21:16:10 2021' FileOwnedByWorkbench=false
Product='HFSS' NextUniqueID=0
MoveBackwards=false
$begin 'Desktop' Version(15, 0)
InfrastructureVersion(1, 0)
$end 'Desktop' $begin 'HFSSEnvironment' Version(1, 0)
$end 'HFSSEnvironment' $begin 'HFIEEnvironment' Version(1, 0)
$end 'HFIEEnvironment' $begin 'geometry3deditor' Version(1, 0)
$end 'geometry3deditor' $begin 'ProjectDatasets' NextUniqueID=0
MoveBackwards=false
DatasetType='ProjectDatasetType' $begin 'DatasetDefinitions' $end 'DatasetDefinitions' $end 'ProjectDatasets' $begin 'Definitions' $begin 'Folders' Definitions(1104, 10000, 1, 1, 0, false, false)
Materials(1104, 9500, 9, 2, 1, false, false)
$end 'Folders' $begin 'Materials' $begin 'vacuum' CoordinateSystemType='Cartesian' $begin 'AttachedData' $end 'AttachedData' $begin 'ModifierData' $end 'ModifierData' permittivity='1' ModTime=1028307964
Library='Materials' LibLocation='SysLibrary' ModSinceLib=false
$end 'vacuum' $begin 'Rogers RT/duroid 5880 (tm)' CoordinateSystemType='Cartesian' $begin 'AttachedData' $end 'AttachedData' $begin 'ModifierData'
$end 'ModifierData' permittivity='2.2' dielectric_loss_tangent='0.0009' ModTime=1028307964
Library='Materials' LibLocation='SysLibrary' ModSinceLib=false
$end 'Rogers RT/duroid 5880 (tm)' $end 'Materials' $begin 'Scripts' $end 'Scripts' $end 'Definitions' DesignIDServer=2
MoveBackwards=false
$begin 'HFSSModel' RepRewriteV2=true
Name='HFSSDesign1' DesignID=0
'Use Advanced DC Extrapolation'=false
'Allow Material Override'=false
'Calculate Lossy Dielectrics'=true
$begin 'TemperatureSettings' IncludeTemperatureDependence=false
EnableFeedback=false
Temperatures(926, '22cel')
$end 'TemperatureSettings' ObjsEnabledForDeformation()
SolutionType='DrivenModal' MaterialDensity=1
MassOfTissue=1
UseAutoDCThickness=true
$begin 'OutputVariable' NextUniqueID=0
MoveBackwards=false
$end 'OutputVariable' $begin 'ModelSetup' $begin 'Editor3D Doc Preferences'
'Plane Background'=true
BackgroundColor1=16777215
BackgroundColor2=0
'Need Lights'=true
'Ambient Light'=8355711
'Num Lights'=2
Light0[4: 8355711, 0.200000002980232, 0.400000005960464, 1]
Light1[4: 8355711, -0.200000002980232, -0.400000005960464, -1]
$end 'Editor3D Doc Preferences' $begin 'DesignDatasets' NextUniqueID=0
MoveBackwards=false
DatasetType='DesignDatasetType' $begin 'DatasetDefinitions' $end 'DatasetDefinitions' $end 'DesignDatasets' SnapMode=31
WorkingCS=1
$begin 'GeometryCore' BlockVersionID=3
DataVersion=31
NativeKernel='ACIS' NativeKernelVersionID=5
Units='mm' InstanceID=-1
$begin 'ValidationOptions' EntityCheckLevel='Strict' IgnoreUnclassifiedObjects=false
SkipIntersectionChecks=false
$end 'ValidationOptions' $begin 'GeometryOperations' BlockVersionID=2
$begin 'AnsoftRangedIDServerManager' $begin 'AnsoftRangedIDServer' IDServerObjectTypeID=0
IDServerRangeMin=0
IDServerRangeMax=2146483647
NextUniqueID=953
MoveBackwards=false
$end 'AnsoftRangedIDServer' $begin 'AnsoftRangedIDServer' IDServerObjectTypeID=1
IDServerRangeMin=2146483648
IDServerRangeMax=2146485547
NextUniqueID=2146483654
MoveBackwards=false
$end 'AnsoftRangedIDServer' $end 'AnsoftRangedIDServerManager' StartBackGroundFaceID=2146483648
$begin 'CoordinateSystems' $end 'CoordinateSystems' $begin 'UserDefinedModels' $end 'UserDefinedModels' $begin 'ToplevelParts' $begin 'GeometryPart' $begin 'Attributes' Name='Substrate' Flags='' Color='(0 0 255)' Transparency=0.86
PartCoordinateSystem=1
UDMId=-1
MaterialValue='"Rogers RT/duroid 5880 (tm)"' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Box' ID=5
ReferenceCoordSystemID=1
$begin 'BoxParameters' KernelVersion=5
XPosition='0mm' YPosition='0mm' ZPosition='0mm' XSize='12mm' YSize='23mm' ZSize='1mm' $end 'BoxParameters' ParentPartID=6
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=6
NumWires=0
NumLoops=6
NumCoedges=24
NumEdges=12
NumVertices=8
$end 'Topology' BodyID=6
StartFaceID=7
StartEdgeID=13
StartVertexID=25
NumNewFaces=6
NumNewEdges=12
NumNewVertices=8
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Ground_Plane' Flags=''
Color='(0 64 128)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='"vacuum"' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=33
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='0mm' YStart='0mm' ZStart='0mm' Width='12mm' Height='23mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=34
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=34
StartFaceID=-1
StartEdgeID=35
StartVertexID=39
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=43
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=34
$end 'LocalOperationParameters' ParentPartID=34
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=44
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=44
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=276
FcUVMid(6, 11.5, 0)
$begin
'FcTolVts' TolVt(0, 0, 0, 0)
TolVt(12, 0, 0, 0)
TolVt(12, 23, 0, 0)
TolVt(0, 23, 0, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=33
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle5' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='"vacuum"' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=141
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='4mm' YStart='3mm' ZStart='1mm' Width='1mm' Height='2mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=142
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology'
NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=142
StartFaceID=-1
StartEdgeID=143
StartVertexID=147
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=151
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=142
$end 'LocalOperationParameters' ParentPartID=142
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=152
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=152
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=2
FcUVMid(4.5, 4, 1)
$begin
'FcTolVts' TolVt(4, 3, 1, 0)
TolVt(5, 3, 1, 0)
TolVt(5, 5, 1, 0)
TolVt(4, 5, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=141
$end 'Operation' $begin 'Operation' OperationType='Unite' ID=694
$begin 'UniteParameters' KernelVersion=5
KeepOriginals=false
BlankPart=142
NumToolParts=1
ToolParts(398)
$end 'UniteParameters' ParentPartID=142
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=8
NumEdges=8
NumVertices=8
$end 'Topology' BodyID=-1
StartFaceID=-1
StartEdgeID=695
StartVertexID=-1
NumNewFaces=0
NumNewEdges=2
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $end 'NewFaces' $begin 'NewEdges' $begin 'Edge' NormalizedSerialNum=0
ID=695
EdgeFaces(152)
$begin 'EdTolVts' TolVt(4, 3, 1, 0)
TolVt(4.35, 3, 1, 0)
$end 'EdTolVts' EdgeMidPoint(4.175, 3, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=1
ID=696
EdgeFaces(152)
$begin 'EdTolVts' TolVt(4.6, 3, 1, 0)
TolVt(5, 3, 1, 0)
$end 'EdTolVts' EdgeMidPoint(4.8, 3, 1)
$end 'Edge' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' BlankOperation=151
NumToolOperations=1
ToolOperations(407)
$end 'Operation' $begin 'Operation' OperationType='Unite' ID=706
$begin 'UniteParameters' KernelVersion=5
KeepOriginals=false
BlankPart=142
NumToolParts=1
ToolParts(94)
$end 'UniteParameters' ParentPartID=142
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=34
NumEdges=34
NumVertices=34
$end 'Topology' BodyID=-1
StartFaceID=-1
StartEdgeID=707
StartVertexID=-1
NumNewFaces=0
NumNewEdges=2
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $end 'NewFaces' $begin 'NewEdges'
$begin 'Edge' NormalizedSerialNum=0
ID=707
EdgeFaces(152)
$begin 'EdTolVts' TolVt(1.6, 2, 1, 0)
TolVt(4.35, 2, 1, 0)
$end 'EdTolVts' EdgeMidPoint(2.975, 2, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=1
ID=708
EdgeFaces(152)
$begin 'EdTolVts' TolVt(4.6, 2, 1, 0)
TolVt(7.35, 2, 1, 0)
$end 'EdTolVts' EdgeMidPoint(5.975, 2, 1)
$end 'Edge' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' BlankOperation=694
NumToolOperations=1
ToolOperations(698)
$end 'Operation' $begin 'Operation' OperationType='Unite' ID=842
$begin 'UniteParameters' KernelVersion=5
KeepOriginals=false
BlankPart=142
NumToolParts=2
ToolParts(795, 518)
$end 'UniteParameters' ParentPartID=142
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=56
NumEdges=56
NumVertices=56
$end 'Topology' BodyID=-1
StartFaceID=-1
StartEdgeID=843
StartVertexID=-1
NumNewFaces=0
NumNewEdges=4
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $end 'NewFaces' $begin 'NewEdges' $begin 'Edge' NormalizedSerialNum=0
ID=843
EdgeFaces(152)
$begin 'EdTolVts' TolVt(3.225, 2, 1, 0)
TolVt(4.35, 2, 1, 0)
$end 'EdTolVts' EdgeMidPoint(3.7875, 2, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=1
ID=844
EdgeFaces(152)
$begin 'EdTolVts' TolVt(3.225, 6.7, 1, 0)
TolVt(10.6, 6.7, 1, 0)
$end 'EdTolVts' EdgeMidPoint(6.9125, 6.7, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=2
ID=845
EdgeFaces(152)
$begin 'EdTolVts' TolVt(1.3, 6.7, 1, 0)
TolVt(2.975, 6.7, 1, 0)
$end 'EdTolVts' EdgeMidPoint(2.1375, 6.7, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=3
ID=846
EdgeFaces(152)
$begin 'EdTolVts' TolVt(1.6, 2, 1, 0)
TolVt(2.975, 2, 1, 0)
$end 'EdTolVts' EdgeMidPoint(2.2875, 2, 1)
$end 'Edge' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' BlankOperation=706
NumToolOperations=2
ToolOperations(804, 709)
$end 'Operation' $begin 'Operation' OperationType='Unite' ID=847
$begin 'UniteParameters' KernelVersion=5
KeepOriginals=false
BlankPart=142
NumToolParts=2
ToolParts(807, 458)
$end 'UniteParameters' ParentPartID=142
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=96
NumEdges=96
NumVertices=96
$end 'Topology' BodyID=-1
StartFaceID=-1
StartEdgeID=848
StartVertexID=-1
NumNewFaces=0
NumNewEdges=4
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $end 'NewFaces' $begin 'NewEdges' $begin 'Edge' NormalizedSerialNum=0
ID=848
EdgeFaces(152)
$begin 'EdTolVts' TolVt(7.35, 6.95, 1, 0)
TolVt(5.5375, 6.95, 1, 0)
$end 'EdTolVts' EdgeMidPoint(6.44375, 6.95, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=1
ID=849
EdgeFaces(152)
$begin 'EdTolVts' TolVt(5.5375, 11.75, 1, 0)
TolVt(10.64, 11.75, 1, 0)
$end 'EdTolVts' EdgeMidPoint(8.08875, 11.75, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=2
ID=850
EdgeFaces(152)
$begin 'EdTolVts' TolVt(1.34, 11.75, 1, 0)
TolVt(5.2875, 11.75, 1, 0)
$end 'EdTolVts'
EdgeMidPoint(3.31375, 11.75, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=3
ID=851
EdgeFaces(152)
$begin 'EdTolVts' TolVt(5.2875, 6.95, 1, 0)
TolVt(4.6, 6.95, 1, 0)
$end 'EdTolVts' EdgeMidPoint(4.94375, 6.95, 1)
$end 'Edge' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' BlankOperation=842
NumToolOperations=2
ToolOperations(816, 756)
$end 'Operation' $begin 'Operation' OperationType='Unite' ID=852
$begin 'UniteParameters' KernelVersion=5
KeepOriginals=false
BlankPart=142
NumToolParts=2
ToolParts(831, 470)
$end 'UniteParameters' ParentPartID=142
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=136
NumEdges=136
NumVertices=136
$end 'Topology' BodyID=-1
StartFaceID=-1
StartEdgeID=853
StartVertexID=857
NumNewFaces=0
NumNewEdges=4
NumNewVertices=2
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $end 'NewFaces' $begin 'NewEdges' $begin 'Edge' NormalizedSerialNum=0
ID=853
EdgeFaces(152)
$begin 'EdTolVts' TolVt(1.3, 16.8, 1, 0)
TolVt(8.2875, 16.8, 1, 0)
$end 'EdTolVts' EdgeMidPoint(4.79375, 16.8, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=1
ID=854
EdgeFaces(152)
$begin 'EdTolVts' TolVt(8.2875, 12, 1, 0)
TolVt(7.6, 12, 1, 0)
$end 'EdTolVts' EdgeMidPoint(7.94375, 12, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=2
ID=855
EdgeFaces(152)
$begin 'EdTolVts' TolVt(10.35, 12, 1, 0)
TolVt(8.5375, 12, 1, 0)
$end 'EdTolVts'
EdgeMidPoint(9.44375, 12, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=3
ID=856
EdgeFaces(152)
$begin 'EdTolVts' TolVt(8.5375, 16.8, 1, 0)
TolVt(10.6, 16.8, 1, 0)
$end 'EdTolVts' EdgeMidPoint(9.56875, 16.8, 1)
$end 'Edge' $end 'NewEdges' $begin 'NewVertices' $begin 'Vertex' NormalizedSerialNum=0
ID=857
VtPos(8.2875, 16.8, 1)
$end 'Vertex' $begin 'Vertex' NormalizedSerialNum=1
ID=858
VtPos(8.5375, 16.8, 1)
$end 'Vertex' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' BlankOperation=847
NumToolOperations=2
ToolOperations(840, 780)
$end 'Operation' $begin 'Operation' OperationType='Unite' ID=871
$begin 'UniteParameters' KernelVersion=5
KeepOriginals=false
BlankPart=142
NumToolParts=4
ToolParts(106, 154, 202, 250)
$end 'UniteParameters' ParentPartID=142
IsSuppressed=false
$begin 'OperationIdentity'
$begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=152
NumEdges=152
NumVertices=152
$end 'Topology' BodyID=-1
StartFaceID=-1
StartEdgeID=872
StartVertexID=-1
NumNewFaces=0
NumNewEdges=8
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $end 'NewFaces' $begin 'NewEdges' $begin 'Edge' NormalizedSerialNum=0
ID=872
EdgeFaces(152)
$begin 'EdTolVts' TolVt(4.6, 8, 1, 0)
TolVt(5, 8, 1, 0)
$end 'EdTolVts' EdgeMidPoint(4.8, 8, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=1
ID=873
EdgeFaces(152)
$begin 'EdTolVts' TolVt(4, 8, 1, 0)
TolVt(4.35, 8, 1, 0)
$end 'EdTolVts' EdgeMidPoint(4.175, 8, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=2
ID=874
EdgeFaces(152)
$begin 'EdTolVts' TolVt(1.6, 8, 1, 0)
TolVt(2, 8, 1, 0)
$end 'EdTolVts' EdgeMidPoint(1.8, 8, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=3
ID=875
EdgeFaces(152)
$begin 'EdTolVts' TolVt(1, 8, 1, 0)
TolVt(1.35, 8, 1, 0)
$end 'EdTolVts' EdgeMidPoint(1.175, 8, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=4
ID=876
EdgeFaces(152)
$begin 'EdTolVts' TolVt(10.6, 8, 1, 0)
TolVt(11, 8, 1, 0)
$end 'EdTolVts' EdgeMidPoint(10.8, 8, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=5
ID=877
EdgeFaces(152)
$begin 'EdTolVts' TolVt(10, 8, 1, 0)
TolVt(10.35, 8, 1, 0)
$end 'EdTolVts' EdgeMidPoint(10.175, 8, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=6
ID=878
EdgeFaces(152)
$begin 'EdTolVts' TolVt(7.6, 8, 1, 0)
TolVt(8, 8, 1, 0)
$end 'EdTolVts' EdgeMidPoint(7.8, 8, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=7
ID=879
EdgeFaces(152)
$begin 'EdTolVts' TolVt(7, 8, 1, 0)
TolVt(7.35, 8, 1, 0)
$end 'EdTolVts' EdgeMidPoint(7.175, 8, 1)
$end 'Edge' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' BlankOperation=852
NumToolOperations=4
ToolOperations(115, 163, 211, 259)
$end 'Operation' $begin 'Operation' OperationType='Unite' ID=880
$begin 'UniteParameters' KernelVersion=5
KeepOriginals=false
BlankPart=142
NumToolParts=1
ToolParts(860)
$end 'UniteParameters' ParentPartID=142
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=156
NumEdges=156
NumVertices=156
$end 'Topology' BodyID=-1
StartFaceID=-1
StartEdgeID=881
StartVertexID=883
NumNewFaces=0
NumNewEdges=2
NumNewVertices=2
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $end 'NewFaces' $begin 'NewEdges' $begin 'Edge' NormalizedSerialNum=0
ID=881
EdgeFaces(152)
$begin 'EdTolVts' TolVt(5.5375, 6.95, 1, 0)
TolVt(5.5375, 10.55, 1, 0)
$end 'EdTolVts' EdgeMidPoint(5.5375, 8.75, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=1
ID=882
EdgeFaces(152)
$begin 'EdTolVts' TolVt(5.5375, 11.05, 1, 0)
TolVt(5.5375, 11.75, 1, 0)
$end 'EdTolVts' EdgeMidPoint(5.5375, 11.4, 1)
$end 'Edge' $end 'NewEdges' $begin 'NewVertices' $begin 'Vertex' NormalizedSerialNum=0
ID=883
VtPos(5.5375, 10.55, 1)
$end 'Vertex' $begin 'Vertex' NormalizedSerialNum=1
ID=884
VtPos(5.5375, 11.05, 1)
$end 'Vertex' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' BlankOperation=871
NumToolOperations=1
ToolOperations(869)
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle41' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='"vacuum"' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=885
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='12mm' YStart='10.55mm' ZStart='1mm' Width='0.449999999999999mm' Height='-1mm' WhichAxis='X' $end 'RectangleParameters' ParentPartID=886
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=886
StartFaceID=-1
StartEdgeID=887
StartVertexID=891
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=895
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=886
$end 'LocalOperationParameters' ParentPartID=886
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=896
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=896
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=0.449999999999999
FcUVMid(12, 10.775, 0.5)
$begin
'FcTolVts' TolVt(12, 10.55, 1, 0)
TolVt(12, 11, 1, 0)
TolVt(12, 11, 1.11022302462516e-016, 0)
TolVt(12, 10.55, 0, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=885
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Radiation_box' Flags='' Color='(255 128 192)' Transparency=0.94
PartCoordinateSystem=1
UDMId=-1
MaterialValue='"vacuum"' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Box' ID=925
ReferenceCoordSystemID=1
$begin 'BoxParameters' KernelVersion=5
XPosition='-3mm'
YPosition='-3mm' ZPosition='-3mm' XSize='16.6mm' YSize='27mm' ZSize='5.65mm' $end 'BoxParameters' ParentPartID=926
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=6
NumWires=0
NumLoops=6
NumCoedges=24
NumEdges=12
NumVertices=8
$end 'Topology' BodyID=926
StartFaceID=927
StartEdgeID=933
StartVertexID=945
NumNewFaces=6
NumNewEdges=12
NumNewVertices=8
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $end 'Operations' $end 'GeometryPart' $end 'ToplevelParts' $begin 'OperandParts' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle1' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle'
ID=93
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='1mm' YStart='3mm' ZStart='1mm' Width='1mm' Height='2mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=94
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=94
StartFaceID=-1
StartEdgeID=95
StartVertexID=99
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=103
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=94
$end 'LocalOperationParameters' ParentPartID=94
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=104
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=104
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=2
FcUVMid(1.5, 4, 1)
$begin
'FcTolVts' TolVt(1, 3, 1, 0)
TolVt(2, 3, 1, 0)
TolVt(2, 5, 1, 0)
TolVt(1, 5, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges'
$begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=93
$end 'Operation' $begin 'Operation' OperationType='Unite' ID=691
$begin 'UniteParameters' KernelVersion=5
KeepOriginals=false
BlankPart=94
NumToolParts=1
ToolParts(374)
$end 'UniteParameters' ParentPartID=94
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=8
NumEdges=8
NumVertices=8
$end 'Topology' BodyID=-1
StartFaceID=-1
StartEdgeID=692
StartVertexID=-1
NumNewFaces=0
NumNewEdges=2
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $end 'NewFaces' $begin 'NewEdges' $begin 'Edge' NormalizedSerialNum=0
ID=692
EdgeFaces(104)
$begin 'EdTolVts' TolVt(1, 3, 1, 0)
TolVt(1.35, 3, 1, 0)
$end 'EdTolVts' EdgeMidPoint(1.175, 3, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=1
ID=693
EdgeFaces(104)
$begin 'EdTolVts' TolVt(1.6, 3, 1, 0)
TolVt(2, 3, 1, 0)
$end 'EdTolVts' EdgeMidPoint(1.8, 3, 1)
$end 'Edge' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' BlankOperation=103
NumToolOperations=1
ToolOperations(383)
$end 'Operation' $begin 'Operation' OperationType='Unite' ID=697
$begin 'UniteParameters' KernelVersion=5
KeepOriginals=false
BlankPart=94
NumToolParts=1
ToolParts(410)
$end 'UniteParameters' ParentPartID=94
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=10
NumEdges=10
NumVertices=10
$end 'Topology'
BodyID=-1
StartFaceID=-1
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=0
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' BlankOperation=691
NumToolOperations=1
ToolOperations(419)
$end 'Operation' $begin 'Operation' OperationType='Unite' ID=698
$begin 'UniteParameters' KernelVersion=5
KeepOriginals=false
BlankPart=94
NumToolParts=4
ToolParts(422, 190, 434, 238)
$end 'UniteParameters' ParentPartID=94
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=26
NumEdges=26
NumVertices=26
$end 'Topology' BodyID=-1
StartFaceID=-1
StartEdgeID=699
StartVertexID=-1
NumNewFaces=0
NumNewEdges=7
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $end 'NewFaces' $begin 'NewEdges' $begin 'Edge' NormalizedSerialNum=0
ID=699
EdgeFaces(104)
$begin 'EdTolVts' TolVt(10.6, 2, 1, 0)
TolVt(10.65, 2, 1, 0)
$end 'EdTolVts' EdgeMidPoint(10.625, 2, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=1
ID=700
EdgeFaces(104)
$begin 'EdTolVts' TolVt(10.6, 3, 1, 0)
TolVt(11, 3, 1, 0)
$end 'EdTolVts' EdgeMidPoint(10.8, 3, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=2
ID=701
EdgeFaces(104)
$begin 'EdTolVts' TolVt(10, 3, 1, 0)
TolVt(10.35, 3, 1, 0)
$end 'EdTolVts' EdgeMidPoint(10.175, 3, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=3
ID=702
EdgeFaces(104)
$begin 'EdTolVts'
TolVt(7.6, 2, 1, 0)
TolVt(10.35, 2, 1, 0)
$end 'EdTolVts' EdgeMidPoint(8.975, 2, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=4
ID=703
EdgeFaces(104)
$begin 'EdTolVts' TolVt(7.6, 3, 1, 0)
TolVt(8, 3, 1, 0)
$end 'EdTolVts' EdgeMidPoint(7.8, 3, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=5
ID=704
EdgeFaces(104)
$begin 'EdTolVts' TolVt(7, 3, 1, 0)
TolVt(7.35, 3, 1, 0)
$end 'EdTolVts' EdgeMidPoint(7.175, 3, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=6
ID=705
EdgeFaces(104)
$begin 'EdTolVts' TolVt(1.6, 2, 1, 0)
TolVt(7.35, 2, 1, 0)
$end 'EdTolVts' EdgeMidPoint(4.475, 2, 1)
$end 'Edge' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' BlankOperation=697
NumToolOperations=4
ToolOperations(431, 199, 443, 247)
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes'
Name='Rectangle2' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=105
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='1mm' YStart='8mm' ZStart='1mm' Width='1mm' Height='2mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=106
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=106
StartFaceID=-1
StartEdgeID=107
StartVertexID=111
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation'
OperationType='CoverLines' ID=115
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=106
$end 'LocalOperationParameters' ParentPartID=106
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=116
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=116
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=2
FcUVMid(1.5, 9, 1)
$begin
'FcTolVts' TolVt(1, 8, 1, 0)
TolVt(2, 8, 1, 0)
TolVt(2, 10, 1, 0)
TolVt(1, 10, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=105
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle3' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=117
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='1mm' YStart='13mm' ZStart='1mm' Width='1mm' Height='2mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=118
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=118
StartFaceID=-1
StartEdgeID=119
StartVertexID=123
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=127
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=118
$end 'LocalOperationParameters' ParentPartID=118
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=128
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=128
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=2
FcUVMid(1.5, 14, 1)
$begin
'FcTolVts' TolVt(1, 13, 1, 0)
TolVt(2, 13, 1, 0)
TolVt(2, 15, 1, 0)
TolVt(1, 15, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=117
$end 'Operation' $begin 'Operation' OperationType='Unite' ID=740
$begin 'UniteParameters' KernelVersion=5
KeepOriginals=false
BlankPart=118
NumToolParts=1
ToolParts(530)
$end 'UniteParameters' ParentPartID=118
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=8
NumEdges=8
NumVertices=8
$end 'Topology' BodyID=-1
StartFaceID=-1
StartEdgeID=741
StartVertexID=-1
NumNewFaces=0
NumNewEdges=2
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $end 'NewFaces' $begin 'NewEdges' $begin 'Edge' NormalizedSerialNum=0
ID=741
EdgeFaces(128)
$begin 'EdTolVts' TolVt(1, 13, 1, 0)
TolVt(1.35, 13, 1, 0)
$end 'EdTolVts' EdgeMidPoint(1.175, 13, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=1
ID=742
EdgeFaces(128)
$begin 'EdTolVts' TolVt(1.6, 13, 1, 0)
TolVt(2, 13, 1, 0)
$end 'EdTolVts' EdgeMidPoint(1.8, 13, 1)
$end 'Edge' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' BlankOperation=127
NumToolOperations=1
ToolOperations(539)
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle4' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=129
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='1mm' YStart='18mm' ZStart='1mm' Width='1mm' Height='2mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=130
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=130
StartFaceID=-1
StartEdgeID=131
StartVertexID=135
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=139
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=130
$end 'LocalOperationParameters' ParentPartID=130
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=140
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces'
$begin 'Face' NormalizedSerialNum=0
ID=140
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=2
FcUVMid(1.5, 19, 1)
$begin
'FcTolVts' TolVt(1, 18, 1, 0)
TolVt(2, 18, 1, 0)
TolVt(2, 20, 1, 0)
TolVt(1, 20, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=129
$end 'Operation' $begin 'Operation' OperationType='Unite' ID=762
$begin 'UniteParameters' KernelVersion=5
KeepOriginals=false
BlankPart=130
NumToolParts=1
ToolParts(578)
$end 'UniteParameters' ParentPartID=130
IsSuppressed=false
$begin 'OperationIdentity'
$begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=8
NumEdges=8
NumVertices=8
$end 'Topology' BodyID=-1
StartFaceID=-1
StartEdgeID=763
StartVertexID=-1
NumNewFaces=0
NumNewEdges=2
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $end 'NewFaces' $begin 'NewEdges' $begin 'Edge' NormalizedSerialNum=0
ID=763
EdgeFaces(140)
$begin 'EdTolVts' TolVt(1, 18, 1, 0)
TolVt(1.35, 18, 1, 0)
$end 'EdTolVts' EdgeMidPoint(1.175, 18, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=1
ID=764
EdgeFaces(140)
$begin 'EdTolVts' TolVt(1.6, 18, 1, 0)
TolVt(2, 18, 1, 0)
$end 'EdTolVts' EdgeMidPoint(1.8, 18, 1)
$end 'Edge' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices'
$end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' BlankOperation=139
NumToolOperations=1
ToolOperations(587)
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle6' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=153
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='4mm' YStart='8mm' ZStart='1mm' Width='1mm' Height='2mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=154
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=154
StartFaceID=-1
StartEdgeID=155
StartVertexID=159
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=163
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=154
$end 'LocalOperationParameters' ParentPartID=154
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=164
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=164
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=2
FcUVMid(4.5, 9, 1)
$begin
'FcTolVts' TolVt(4, 8, 1, 0)
TolVt(5, 8, 1, 0)
TolVt(5, 10, 1, 0)
TolVt(4, 10, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=153
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle7' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=165
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='4mm' YStart='13mm' ZStart='1mm' Width='1mm' Height='2mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=166
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=166
StartFaceID=-1
StartEdgeID=167
StartVertexID=171
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=175
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=166
$end 'LocalOperationParameters' ParentPartID=166
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=176
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=176
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=2
FcUVMid(4.5, 14, 1)
$begin
'FcTolVts' TolVt(4, 13, 1, 0)
TolVt(5, 13, 1, 0)
TolVt(5, 15, 1, 0)
TolVt(4, 15, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices'
$end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=165
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle8' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=177
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='4mm' YStart='18mm' ZStart='1mm' Width='1mm' Height='2mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=178
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=178
StartFaceID=-1
StartEdgeID=179
StartVertexID=183
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=187
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=178
$end 'LocalOperationParameters' ParentPartID=178
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=188
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=188
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=2
FcUVMid(4.5, 19, 1)
$begin
'FcTolVts' TolVt(4, 18, 1, 0)
TolVt(5, 18, 1, 0)
TolVt(5, 20, 1, 0)
TolVt(4, 20, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=177
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle9' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=189
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='7mm'
YStart='3mm' ZStart='1mm' Width='1mm' Height='2mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=190
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=190
StartFaceID=-1
StartEdgeID=191
StartVertexID=195
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=199
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=190
$end 'LocalOperationParameters' ParentPartID=190
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=200
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=200
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=2
FcUVMid(7.5, 4, 1)
$begin
'FcTolVts' TolVt(7, 3, 1, 0)
TolVt(8, 3, 1, 0)
TolVt(8, 5, 1, 0)
TolVt(7, 5, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity'
ParentOperationID=189
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle10' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=201
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='7mm' YStart='8mm' ZStart='1mm' Width='1mm' Height='2mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=202
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=202
StartFaceID=-1
StartEdgeID=203
StartVertexID=207
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=211
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=202
$end 'LocalOperationParameters' ParentPartID=202
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=212
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=212
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=2
FcUVMid(7.5, 9, 1)
$begin
'FcTolVts' TolVt(7, 8, 1, 0)
TolVt(8, 8, 1, 0)
TolVt(8, 10, 1, 0)
TolVt(7, 10, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=201
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle11' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=213
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='7mm' YStart='13mm' ZStart='1mm'
Width='1mm' Height='2mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=214
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=214
StartFaceID=-1
StartEdgeID=215
StartVertexID=219
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=223
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=214
$end 'LocalOperationParameters' ParentPartID=214
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology'
BodyID=-1
StartFaceID=224
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=224
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=2
FcUVMid(7.5, 14, 1)
$begin
'FcTolVts' TolVt(7, 13, 1, 0)
TolVt(8, 13, 1, 0)
TolVt(8, 15, 1, 0)
TolVt(7, 15, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=213
$end 'Operation'
$begin 'Operation' OperationType='Unite' ID=746
$begin 'UniteParameters' KernelVersion=5
KeepOriginals=false
BlankPart=214
NumToolParts=1
ToolParts(554)
$end 'UniteParameters' ParentPartID=214
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=8
NumEdges=8
NumVertices=8
$end 'Topology' BodyID=-1
StartFaceID=-1
StartEdgeID=747
StartVertexID=-1
NumNewFaces=0
NumNewEdges=2
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $end 'NewFaces' $begin 'NewEdges' $begin 'Edge' NormalizedSerialNum=0
ID=747
EdgeFaces(224)
$begin 'EdTolVts' TolVt(7, 13, 1, 0)
TolVt(7.35, 13, 1, 0)
$end 'EdTolVts' EdgeMidPoint(7.175, 13, 1)
$end 'Edge' $begin 'Edge'
NormalizedSerialNum=1
ID=748
EdgeFaces(224)
$begin 'EdTolVts' TolVt(7.6, 13, 1, 0)
TolVt(8, 13, 1, 0)
$end 'EdTolVts' EdgeMidPoint(7.8, 13, 1)
$end 'Edge' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' BlankOperation=223
NumToolOperations=1
ToolOperations(563)
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle12' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=225
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='7mm' YStart='18mm' ZStart='1mm' Width='1mm' Height='2mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=226
IsSuppressed=false
$begin 'OperationIdentity'
$begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=226
StartFaceID=-1
StartEdgeID=227
StartVertexID=231
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=235
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=226
$end 'LocalOperationParameters' ParentPartID=226
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=236
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=236
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=2
FcUVMid(7.5, 19, 1)
$begin
'FcTolVts' TolVt(7, 18, 1, 0)
TolVt(8, 18, 1, 0)
TolVt(8, 20, 1, 0)
TolVt(7, 20, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=225
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle13' Flags='' Color='(132 132 193)'
Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=237
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='10mm' YStart='3mm' ZStart='1mm' Width='1mm' Height='2mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=238
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=238
StartFaceID=-1
StartEdgeID=239
StartVertexID=243
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=247
$begin 'LocalOperationParameters'
KernelVersion=5
LocalOpPart=238
$end 'LocalOperationParameters' ParentPartID=238
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=248
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=248
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=2
FcUVMid(10.5, 4, 1)
$begin
'FcTolVts' TolVt(10, 3, 1, 0)
TolVt(11, 3, 1, 0)
TolVt(11, 5, 1, 0)
TolVt(10, 5, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=237
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle14' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=249
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='10mm' YStart='8mm' ZStart='1mm' Width='1mm' Height='2mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=250
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=250
StartFaceID=-1
StartEdgeID=251
StartVertexID=255
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=259
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=250
$end 'LocalOperationParameters' ParentPartID=250
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=260
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=260
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=2
FcUVMid(10.5, 9, 1)
$begin
'FcTolVts' TolVt(10, 8, 1, 0)
TolVt(11, 8, 1, 0)
TolVt(11, 10, 1, 0)
TolVt(10, 10, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=249
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle15' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=261
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='10mm' YStart='13mm' ZStart='1mm' Width='1mm' Height='2mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=262
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=262
StartFaceID=-1
StartEdgeID=263
StartVertexID=267
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=271
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=262
$end 'LocalOperationParameters'
ParentPartID=262
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=272
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=272
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=2
FcUVMid(10.5, 14, 1)
$begin
'FcTolVts' TolVt(10, 13, 1, 0)
TolVt(11, 13, 1, 0)
TolVt(11, 15, 1, 0)
TolVt(10, 15, 1, 0)
$end
'FcTolVts'
$end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=261
$end 'Operation' $begin 'Operation' OperationType='Unite' ID=753
$begin 'UniteParameters' KernelVersion=5
KeepOriginals=false
BlankPart=262
NumToolParts=1
ToolParts(566)
$end 'UniteParameters' ParentPartID=262
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=8
NumEdges=8
NumVertices=8
$end 'Topology' BodyID=-1
StartFaceID=-1
StartEdgeID=754
StartVertexID=-1
NumNewFaces=0
NumNewEdges=2
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper'
$begin 'NewFaces' $end 'NewFaces' $begin 'NewEdges' $begin 'Edge' NormalizedSerialNum=0
ID=754
EdgeFaces(272)
$begin 'EdTolVts' TolVt(10, 13, 1, 0)
TolVt(10.35, 13, 1, 0)
$end 'EdTolVts' EdgeMidPoint(10.175, 13, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=1
ID=755
EdgeFaces(272)
$begin 'EdTolVts' TolVt(10.6, 13, 1, 0)
TolVt(11, 13, 1, 0)
$end 'EdTolVts' EdgeMidPoint(10.8, 13, 1)
$end 'Edge' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' BlankOperation=271
NumToolOperations=1
ToolOperations(575)
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle16' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations'
$begin 'Operation' OperationType='Rectangle' ID=273
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='10mm' YStart='18mm' ZStart='1mm' Width='1mm' Height='2mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=274
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=274
StartFaceID=-1
StartEdgeID=275
StartVertexID=279
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=283
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=274
$end 'LocalOperationParameters' ParentPartID=274
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology'
NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=284
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=284
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=2
FcUVMid(10.5, 19, 1)
$begin
'FcTolVts' TolVt(10, 18, 1, 0)
TolVt(11, 18, 1, 0)
TolVt(11, 20, 1, 0)
TolVt(10, 20, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces'
$begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=273
$end 'Operation' $begin 'Operation' OperationType='Unite' ID=771
$begin 'UniteParameters' KernelVersion=5
KeepOriginals=false
BlankPart=274
NumToolParts=1
ToolParts(614)
$end 'UniteParameters' ParentPartID=274
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=8
NumEdges=8
NumVertices=8
$end 'Topology' BodyID=-1
StartFaceID=-1
StartEdgeID=772
StartVertexID=-1
NumNewFaces=0
NumNewEdges=2
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $end 'NewFaces' $begin 'NewEdges' $begin 'Edge' NormalizedSerialNum=0
ID=772
EdgeFaces(284)
$begin 'EdTolVts' TolVt(10, 18, 1, 0)
TolVt(10.3, 18, 1, 0)
$end 'EdTolVts' EdgeMidPoint(10.15, 18, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=1
ID=773
EdgeFaces(284)
$begin 'EdTolVts' TolVt(10.55, 18, 1, 0)
TolVt(11, 18, 1, 0)
$end 'EdTolVts' EdgeMidPoint(10.775, 18, 1)
$end 'Edge' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' BlankOperation=283
NumToolOperations=1
ToolOperations(623)
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle17' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=373
ReferenceCoordSystemID=1
$begin 'RectangleParameters'
KernelVersion=5
XStart='1.35mm' YStart='3mm' ZStart='1mm' Width='0.25mm' Height='-1mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=374
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=374
StartFaceID=-1
StartEdgeID=375
StartVertexID=379
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=383
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=374
$end 'LocalOperationParameters' ParentPartID=374
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=384
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=384
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=0.25
FcUVMid(1.475, 2.5, 1)
$begin
'FcTolVts' TolVt(1.35, 3, 1, 0)
TolVt(1.6, 3, 1, 0)
TolVt(1.6, 2, 1, 0)
TolVt(1.35, 2, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices'
$end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=373
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle18' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=397
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='4.35mm' YStart='3mm' ZStart='1mm' Width='0.25mm' Height='-1mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=398
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=398
StartFaceID=-1
StartEdgeID=399
StartVertexID=403
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=407
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=398
$end 'LocalOperationParameters' ParentPartID=398
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=408
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=408
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=0.25
FcUVMid(4.475, 2.5, 1)
$begin
'FcTolVts' TolVt(4.35, 3, 1, 0)
TolVt(4.6, 3, 1, 0)
TolVt(4.6, 2, 1, 0)
TolVt(4.35, 2, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=397
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle19' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=409
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='1.35mm'
YStart='2mm' ZStart='1mm' Width='9.3mm' Height='-0.25mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=410
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=410
StartFaceID=-1
StartEdgeID=411
StartVertexID=415
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=419
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=410
$end 'LocalOperationParameters' ParentPartID=410
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=420
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=420
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=2.325
FcUVMid(6, 1.875, 1)
$begin
'FcTolVts' TolVt(1.35, 2, 1, 0)
TolVt(10.65, 2, 1, 0)
TolVt(10.65, 1.75, 1, 0)
TolVt(1.35, 1.75, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity'
ParentOperationID=409
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle20' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=421
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='7.35mm' YStart='3mm' ZStart='1mm' Width='0.25mm' Height='-1mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=422
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=422
StartFaceID=-1
StartEdgeID=423
StartVertexID=427
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=431
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=422
$end 'LocalOperationParameters' ParentPartID=422
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=432
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=432
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=0.25
FcUVMid(7.475, 2.5, 1)
$begin
'FcTolVts' TolVt(7.35, 3, 1, 0)
TolVt(7.6, 3, 1, 0)
TolVt(7.6, 2, 1, 0)
TolVt(7.35, 2, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=421
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle21' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=433
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='10.35mm' YStart='3mm' ZStart='1mm'
Width='0.25mm' Height='-1mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=434
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=434
StartFaceID=-1
StartEdgeID=435
StartVertexID=439
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=443
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=434
$end 'LocalOperationParameters' ParentPartID=434
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology'
BodyID=-1
StartFaceID=444
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=444
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=0.25
FcUVMid(10.475, 2.5, 1)
$begin
'FcTolVts' TolVt(10.35, 3, 1, 0)
TolVt(10.6, 3, 1, 0)
TolVt(10.6, 2, 1, 0)
TolVt(10.35, 2, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=433
$end 'Operation'
$end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle22' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=445
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='1.3mm' YStart='6.7mm' ZStart='1mm' Width='9.3mm' Height='0.25mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=446
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=446
StartFaceID=-1
StartEdgeID=447
StartVertexID=451
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=455
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=446
$end 'LocalOperationParameters' ParentPartID=446
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=456
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=456
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=2.325
FcUVMid(5.95, 6.825, 1)
$begin
'FcTolVts'
TolVt(1.3, 6.7, 1, 0)
TolVt(10.6, 6.7, 1, 0)
TolVt(10.6, 6.95, 1, 0)
TolVt(1.3, 6.95, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=445
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle23' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=457
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='1.34mm' YStart='11.75mm' ZStart='1mm' Width='9.3mm' Height='0.25mm'
WhichAxis='Z' $end 'RectangleParameters' ParentPartID=458
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=458
StartFaceID=-1
StartEdgeID=459
StartVertexID=463
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=467
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=458
$end 'LocalOperationParameters' ParentPartID=458
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=468
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=468
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=2.325
FcUVMid(5.99, 11.875, 1)
$begin
'FcTolVts' TolVt(1.34, 11.75, 1, 0)
TolVt(10.64, 11.75, 1, 0)
TolVt(10.64, 12, 1, 0)
TolVt(1.34, 12, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=457
$end 'Operation' $begin 'Operation' OperationType='Unite'
ID=756
$begin 'UniteParameters' KernelVersion=5
KeepOriginals=false
BlankPart=458
NumToolParts=4
ToolParts(118, 542, 214, 262)
$end 'UniteParameters' ParentPartID=458
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=36
NumEdges=36
NumVertices=36
$end 'Topology' BodyID=-1
StartFaceID=-1
StartEdgeID=757
StartVertexID=-1
NumNewFaces=0
NumNewEdges=5
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $end 'NewFaces' $begin 'NewEdges' $begin 'Edge' NormalizedSerialNum=0
ID=757
EdgeFaces(468)
$begin 'EdTolVts' TolVt(10.64, 12, 1, 0)
TolVt(10.6, 12, 1, 0)
$end 'EdTolVts' EdgeMidPoint(10.62, 12, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=1
ID=758
EdgeFaces(468)
$begin 'EdTolVts' TolVt(10.35, 12, 1, 0)
TolVt(7.6, 12, 1, 0)
$end 'EdTolVts' EdgeMidPoint(8.975, 12, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=2
ID=759
EdgeFaces(468)
$begin 'EdTolVts' TolVt(7.35, 12, 1, 0)
TolVt(4.6, 12, 1, 0)
$end 'EdTolVts' EdgeMidPoint(5.975, 12, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=3
ID=760
EdgeFaces(468)
$begin 'EdTolVts' TolVt(4.35, 12, 1, 0)
TolVt(1.6, 12, 1, 0)
$end 'EdTolVts' EdgeMidPoint(2.975, 12, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=4
ID=761
EdgeFaces(468)
$begin 'EdTolVts' TolVt(1.35, 12, 1, 0)
TolVt(1.34, 12, 1, 0)
$end 'EdTolVts' EdgeMidPoint(1.345, 12, 1)
$end 'Edge' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' BlankOperation=467
NumToolOperations=4
ToolOperations(740, 743, 746, 753)
$end 'Operation'
$end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle24' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=469
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='1.3mm' YStart='16.8mm' ZStart='1mm' Width='9.3mm' Height='0.25mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=470
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=470
StartFaceID=-1
StartEdgeID=471
StartVertexID=475
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=479
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=470
$end 'LocalOperationParameters' ParentPartID=470
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=480
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=480
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=2.325
FcUVMid(5.95, 16.925, 1)
$begin
'FcTolVts'
TolVt(1.3, 16.8, 1, 0)
TolVt(10.6, 16.8, 1, 0)
TolVt(10.6, 17.05, 1, 0)
TolVt(1.3, 17.05, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=469
$end 'Operation' $begin 'Operation' OperationType='Unite' ID=780
$begin 'UniteParameters' KernelVersion=5
KeepOriginals=false
BlankPart=470
NumToolParts=4
ToolParts(130, 590, 602, 274)
$end 'UniteParameters' ParentPartID=470
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=36
NumEdges=36
NumVertices=36
$end 'Topology' BodyID=-1
StartFaceID=-1
StartEdgeID=781
StartVertexID=786
NumNewFaces=0
NumNewEdges=5
NumNewVertices=8
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $end 'NewFaces' $begin 'NewEdges' $begin 'Edge' NormalizedSerialNum=0
ID=781
EdgeFaces(480)
$begin 'EdTolVts' TolVt(10.6, 17.05, 1, 0)
TolVt(10.55, 17.05, 1, 0)
$end 'EdTolVts' EdgeMidPoint(10.575, 17.05, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=1
ID=782
EdgeFaces(480)
$begin 'EdTolVts' TolVt(10.3, 17.05, 1, 0)
TolVt(7.55, 17.05, 1, 0)
$end 'EdTolVts' EdgeMidPoint(8.925, 17.05, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=2
ID=783
EdgeFaces(480)
$begin 'EdTolVts' TolVt(7.3, 17.05, 1, 0)
TolVt(4.6, 17.05, 1, 0)
$end 'EdTolVts'
EdgeMidPoint(5.95, 17.05, 1) $end 'Edge' $begin 'Edge' NormalizedSerialNum=3 ID=784 EdgeFaces(480) $begin 'EdTolVts' TolVt(4.35, 17.05, 1, 0) TolVt(1.6, 17.05, 1, 0) $end 'EdTolVts' EdgeMidPoint(2.975, 17.05, 1) $end 'Edge' $begin 'Edge' NormalizedSerialNum=4 ID=785 EdgeFaces(480) $begin 'EdTolVts' TolVt(1.35, 17.05, 1, 0) TolVt(1.3, 17.05, 1, 0) $end 'EdTolVts' EdgeMidPoint(1.325, 17.05, 1) $end 'Edge' $end 'NewEdges' $begin 'NewVertices' $begin 'Vertex' NormalizedSerialNum=0 ID=786 VtPos(10.55, 17.05, 1) $end 'Vertex' $begin 'Vertex' NormalizedSerialNum=1 ID=787 VtPos(10.3, 17.05, 1) $end 'Vertex' $begin 'Vertex' NormalizedSerialNum=2 ID=788 VtPos(7.55, 17.05, 1) $end 'Vertex' $begin 'Vertex' NormalizedSerialNum=3 ID=789
VtPos(7.3, 17.05, 1)
$end 'Vertex' $begin 'Vertex' NormalizedSerialNum=4
ID=790
VtPos(4.6, 17.05, 1)
$end 'Vertex' $begin 'Vertex' NormalizedSerialNum=5
ID=791
VtPos(4.35, 17.05, 1)
$end 'Vertex' $begin 'Vertex' NormalizedSerialNum=6
ID=792
VtPos(1.6, 17.05, 1)
$end 'Vertex' $begin 'Vertex' NormalizedSerialNum=7
ID=793
VtPos(1.35, 17.05, 1)
$end 'Vertex' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' BlankOperation=479
NumToolOperations=4
ToolOperations(762, 765, 768, 771)
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle25' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=481
ReferenceCoordSystemID=1
$begin 'RectangleParameters'
KernelVersion=5
XStart='1.35mm' YStart='8mm' ZStart='1mm' Width='0.25mm' Height='-1.1mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=482
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=482
StartFaceID=-1
StartEdgeID=483
StartVertexID=487
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=491
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=482
$end 'LocalOperationParameters' ParentPartID=482
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=492
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=492
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=0.275
FcUVMid(1.475, 7.45, 1)
$begin
'FcTolVts' TolVt(1.35, 8, 1, 0)
TolVt(1.6, 8, 1, 0)
TolVt(1.6, 6.9, 1, 0)
TolVt(1.35, 6.9, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices'
$end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=481
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle26' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=493
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='4.35mm' YStart='8mm' ZStart='1mm' Width='0.25mm' Height='-1.1mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=494
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=494
StartFaceID=-1
StartEdgeID=495
StartVertexID=499
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=503
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=494
$end 'LocalOperationParameters' ParentPartID=494
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=504
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=504
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=0.275
FcUVMid(4.475, 7.45, 1)
$begin
'FcTolVts' TolVt(4.35, 8, 1, 0)
TolVt(4.6, 8, 1, 0)
TolVt(4.6, 6.9, 1, 0)
TolVt(4.35, 6.9, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=493
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle27' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=505
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='7.35mm'
YStart='8mm' ZStart='1mm' Width='0.25mm' Height='-1.1mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=506
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=506
StartFaceID=-1
StartEdgeID=507
StartVertexID=511
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=515
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=506
$end 'LocalOperationParameters' ParentPartID=506
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=516
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=516
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=0.275
FcUVMid(7.475, 7.45, 1)
$begin
'FcTolVts' TolVt(7.35, 8, 1, 0)
TolVt(7.6, 8, 1, 0)
TolVt(7.6, 6.9, 1, 0)
TolVt(7.35, 6.9, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity'
ParentOperationID=505
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle28' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=517
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='10.35mm' YStart='8mm' ZStart='1mm' Width='0.25mm' Height='-1.1mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=518
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=518
StartFaceID=-1
StartEdgeID=519
StartVertexID=523
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=527
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=518
$end 'LocalOperationParameters' ParentPartID=518
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=528
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=528
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=0.275
FcUVMid(10.475, 7.45, 1)
$begin
'FcTolVts' TolVt(10.35, 8, 1, 0)
TolVt(10.6, 8, 1, 0)
TolVt(10.6, 6.9, 1, 0)
TolVt(10.35, 6.9, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=517
$end 'Operation' $begin 'Operation' OperationType='Unite' ID=709
$begin 'UniteParameters' KernelVersion=5
KeepOriginals=false
BlankPart=518
NumToolParts=4
ToolParts(446, 506, 494, 482)
$end 'UniteParameters' ParentPartID=518
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=18
NumEdges=18
NumVertices=18
$end 'Topology'
BodyID=-1
StartFaceID=-1
StartEdgeID=710
StartVertexID=714
NumNewFaces=0
NumNewEdges=4
NumNewVertices=7
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $end 'NewFaces' $begin 'NewEdges' $begin 'Edge' NormalizedSerialNum=0
ID=710
EdgeFaces(528)
$begin 'EdTolVts' TolVt(1.35, 6.95, 1, 0)
TolVt(1.3, 6.95, 1, 0)
$end 'EdTolVts' EdgeMidPoint(1.325, 6.95, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=1
ID=711
EdgeFaces(528)
$begin 'EdTolVts' TolVt(4.35, 6.95, 1, 0)
TolVt(1.6, 6.95, 1, 0)
$end 'EdTolVts' EdgeMidPoint(2.975, 6.95, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=2
ID=712
EdgeFaces(528)
$begin 'EdTolVts' TolVt(7.35, 6.95, 1, 0)
TolVt(4.6, 6.95, 1, 0)
$end 'EdTolVts'
EdgeMidPoint(5.975, 6.95, 1) $end 'Edge' $begin 'Edge' NormalizedSerialNum=3 ID=713 EdgeFaces(528) $begin 'EdTolVts' TolVt(10.35, 6.95, 1, 0) TolVt(7.6, 6.95, 1, 0) $end 'EdTolVts' EdgeMidPoint(8.975, 6.95, 1) $end 'Edge' $end 'NewEdges' $begin 'NewVertices' $begin 'Vertex' NormalizedSerialNum=0 ID=714 VtPos(1.35, 6.95, 1) $end 'Vertex' $begin 'Vertex' NormalizedSerialNum=1 ID=715 VtPos(1.6, 6.95, 1) $end 'Vertex' $begin 'Vertex' NormalizedSerialNum=2 ID=716 VtPos(4.35, 6.95, 1) $end 'Vertex' $begin 'Vertex' NormalizedSerialNum=3 ID=717 VtPos(4.6, 6.95, 1) $end 'Vertex' $begin 'Vertex' NormalizedSerialNum=4 ID=718 VtPos(7.35, 6.95, 1) $end 'Vertex' $begin 'Vertex' NormalizedSerialNum=5 ID=719 VtPos(7.6, 6.95, 1) $end 'Vertex' $begin 'Vertex' NormalizedSerialNum=6
ID=720
VtPos(10.35, 6.95, 1)
$end 'Vertex' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' BlankOperation=527
NumToolOperations=4
ToolOperations(455, 515, 503, 491)
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle29' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=529
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='1.35mm' YStart='13mm' ZStart='1mm' Width='0.25mm' Height='-1mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=530
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=530
StartFaceID=-1
StartEdgeID=531
StartVertexID=535
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=539
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=530
$end 'LocalOperationParameters' ParentPartID=530
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=540
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=540
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=0.25
FcUVMid(1.475, 12.5, 1)
$begin
'FcTolVts' TolVt(1.35, 13, 1, 0)
TolVt(1.6, 13, 1, 0)
TolVt(1.6, 12, 1, 0)
TolVt(1.35, 12, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=529
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle30' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation'
OperationType='Rectangle' ID=541
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='4.35mm' YStart='13mm' ZStart='1mm' Width='0.25mm' Height='-1mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=542
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=542
StartFaceID=-1
StartEdgeID=543
StartVertexID=547
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=551
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=542
$end 'LocalOperationParameters' ParentPartID=542
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=552
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=552
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=0.25
FcUVMid(4.475, 12.5, 1)
$begin
'FcTolVts' TolVt(4.35, 13, 1, 0)
TolVt(4.6, 13, 1, 0)
TolVt(4.6, 12, 1, 0)
TolVt(4.35, 12, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges'
$end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=541
$end 'Operation' $begin 'Operation' OperationType='Unite' ID=743
$begin 'UniteParameters' KernelVersion=5
KeepOriginals=false
BlankPart=542
NumToolParts=1
ToolParts(166)
$end 'UniteParameters' ParentPartID=542
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=8
NumEdges=8
NumVertices=8
$end 'Topology' BodyID=-1
StartFaceID=-1
StartEdgeID=744
StartVertexID=-1
NumNewFaces=0
NumNewEdges=2
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $end 'NewFaces' $begin 'NewEdges' $begin 'Edge' NormalizedSerialNum=0
ID=744
EdgeFaces(552)
$begin 'EdTolVts' TolVt(4, 13, 1, 0)
TolVt(4.35, 13, 1, 0)
$end 'EdTolVts' EdgeMidPoint(4.175, 13, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=1
ID=745
EdgeFaces(552)
$begin 'EdTolVts' TolVt(4.6, 13, 1, 0)
TolVt(5, 13, 1, 0)
$end 'EdTolVts' EdgeMidPoint(4.8, 13, 1)
$end 'Edge' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' BlankOperation=551
NumToolOperations=1
ToolOperations(175)
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle31' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=553
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='7.35mm' YStart='13mm'
ZStart='1mm' Width='0.25mm' Height='-1mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=554
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=554
StartFaceID=-1
StartEdgeID=555
StartVertexID=559
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=563
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=554
$end 'LocalOperationParameters' ParentPartID=554
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=564
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=564
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=0.25
FcUVMid(7.475, 12.5, 1)
$begin
'FcTolVts' TolVt(7.35, 13, 1, 0)
TolVt(7.6, 13, 1, 0)
TolVt(7.6, 12, 1, 0)
TolVt(7.35, 12, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=553
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle32' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=565
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='10.35mm' YStart='13mm' ZStart='1mm' Width='0.25mm' Height='-1mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=566
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=566
StartFaceID=-1
StartEdgeID=567
StartVertexID=571
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=575
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=566
$end 'LocalOperationParameters' ParentPartID=566
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=576
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=576
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=0.25
FcUVMid(10.475, 12.5, 1)
$begin
'FcTolVts'
TolVt(10.35, 13, 1, 0)
TolVt(10.6, 13, 1, 0)
TolVt(10.6, 12, 1, 0)
TolVt(10.35, 12, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=565
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle33' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=577
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='1.35mm' YStart='18mm' ZStart='1mm' Width='0.25mm' Height='-1mm'
WhichAxis='Z' $end 'RectangleParameters' ParentPartID=578
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=578
StartFaceID=-1
StartEdgeID=579
StartVertexID=583
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=587
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=578
$end 'LocalOperationParameters' ParentPartID=578
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=588
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=588
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=0.25
FcUVMid(1.475, 17.5, 1)
$begin
'FcTolVts' TolVt(1.35, 18, 1, 0)
TolVt(1.6, 18, 1, 0)
TolVt(1.6, 17, 1, 0)
TolVt(1.35, 17, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=577
$end 'Operation' $end 'Operations' $end 'GeometryPart'
$begin 'GeometryPart' $begin 'Attributes' Name='Rectangle34' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=589
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='4.35mm' YStart='18mm' ZStart='1mm' Width='0.25mm' Height='-1mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=590
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=590
StartFaceID=-1
StartEdgeID=591
StartVertexID=595
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity'
$end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=599
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=590
$end 'LocalOperationParameters' ParentPartID=590
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=600
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=600
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=0.25
FcUVMid(4.475, 17.5, 1)
$begin
'FcTolVts' TolVt(4.35, 18, 1, 0)
TolVt(4.6, 18, 1, 0)
TolVt(4.6, 17, 1, 0)
TolVt(4.35, 17, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=589
$end 'Operation' $begin 'Operation' OperationType='Unite' ID=765
$begin 'UniteParameters' KernelVersion=5
KeepOriginals=false
BlankPart=590
NumToolParts=1
ToolParts(178)
$end 'UniteParameters' ParentPartID=590
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=8
NumEdges=8
NumVertices=8
$end 'Topology' BodyID=-1
StartFaceID=-1
StartEdgeID=766
StartVertexID=-1
NumNewFaces=0
NumNewEdges=2
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $end 'NewFaces' $begin 'NewEdges' $begin 'Edge' NormalizedSerialNum=0
ID=766
EdgeFaces(600)
$begin 'EdTolVts' TolVt(4, 18, 1, 0)
TolVt(4.35, 18, 1, 0)
$end 'EdTolVts' EdgeMidPoint(4.175, 18, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=1
ID=767
EdgeFaces(600)
$begin 'EdTolVts' TolVt(4.6, 18, 1, 0)
TolVt(5, 18, 1, 0)
$end 'EdTolVts' EdgeMidPoint(4.8, 18, 1)
$end 'Edge' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' BlankOperation=599
NumToolOperations=1
ToolOperations(187)
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle35' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=601
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='7.55mm' YStart='18mm' ZStart='1mm' Width='-0.25mm' Height='-1mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=602
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=602
StartFaceID=-1
StartEdgeID=603
StartVertexID=607
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=611
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=602
$end 'LocalOperationParameters' ParentPartID=602
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=612
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=612
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=0.25
FcUVMid(7.425, 17.5, 1)
$begin
'FcTolVts' TolVt(7.55, 18, 1, 0)
TolVt(7.3, 18, 1, 0)
TolVt(7.3, 17, 1, 0)
TolVt(7.55, 17, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=601
$end 'Operation' $begin 'Operation' OperationType='Unite' ID=768
$begin 'UniteParameters' KernelVersion=5
KeepOriginals=false
BlankPart=602
NumToolParts=1
ToolParts(226)
$end 'UniteParameters' ParentPartID=602
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=8
NumEdges=8
NumVertices=8
$end 'Topology' BodyID=-1
StartFaceID=-1
StartEdgeID=769
StartVertexID=-1
NumNewFaces=0
NumNewEdges=2
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $end 'NewFaces' $begin 'NewEdges' $begin 'Edge' NormalizedSerialNum=0
ID=769
EdgeFaces(612)
$begin 'EdTolVts' TolVt(7.55, 18, 1, 0)
TolVt(8, 18, 1, 0)
$end 'EdTolVts' EdgeMidPoint(7.775, 18, 1)
$end 'Edge' $begin 'Edge' NormalizedSerialNum=1
ID=770
EdgeFaces(612)
$begin 'EdTolVts' TolVt(7, 18, 1, 0)
TolVt(7.3, 18, 1, 0)
$end 'EdTolVts' EdgeMidPoint(7.15, 18, 1)
$end 'Edge' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' BlankOperation=611
NumToolOperations=1
ToolOperations(235)
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle36' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations'
$begin 'Operation' OperationType='Rectangle' ID=613
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='10.55mm' YStart='18mm' ZStart='1mm' Width='-0.25mm' Height='-1mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=614
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=614
StartFaceID=-1
StartEdgeID=615
StartVertexID=619
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=623
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=614
$end 'LocalOperationParameters' ParentPartID=614
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology'
NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=624
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=624
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=0.25
FcUVMid(10.425, 17.5, 1)
$begin
'FcTolVts' TolVt(10.55, 18, 1, 0)
TolVt(10.3, 18, 1, 0)
TolVt(10.3, 17, 1, 0)
TolVt(10.55, 17, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces'
$begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=613
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle37' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=794
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='2.975mm' YStart='2mm' ZStart='1mm' Width='0.25mm' Height='4.7mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=795
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology'
BodyID=795
StartFaceID=-1
StartEdgeID=796
StartVertexID=800
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=804
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=795
$end 'LocalOperationParameters' ParentPartID=795
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=805
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=805
$begin 'FaceGeomTopol'
FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=1.175
FcUVMid(3.1, 4.35, 1)
$begin
'FcTolVts' TolVt(2.975, 2, 1, 0)
TolVt(3.225, 2, 1, 0)
TolVt(3.225, 6.7, 1, 0)
TolVt(2.975, 6.7, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=794
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle38' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=806
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='5.2875mm' YStart='6.95mm' ZStart='1mm' Width='0.25mm' Height='4.8mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=807
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=807
StartFaceID=-1
StartEdgeID=808
StartVertexID=812
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=816
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=807
$end 'LocalOperationParameters' ParentPartID=807
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=817
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=817
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=1.2
FcUVMid(5.4125, 9.35, 1)
$begin
'FcTolVts' TolVt(5.2875, 6.95, 1, 0)
TolVt(5.5375, 6.95, 1, 0)
TolVt(5.5375, 11.75, 1, 0)
TolVt(5.2875, 11.75, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices'
$end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=806
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle39' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=830
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='8.2875mm' YStart='12mm' ZStart='1mm' Width='0.25mm' Height='4.85mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=831
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=831
StartFaceID=-1
StartEdgeID=832
StartVertexID=836
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=840
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=831
$end 'LocalOperationParameters' ParentPartID=831
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=841
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=841
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry'
Area=1.2125
FcUVMid(8.4125, 14.425, 1)
$begin
'FcTolVts' TolVt(8.2875, 12, 1, 0)
TolVt(8.5375, 12, 1, 0)
TolVt(8.5375, 16.85, 1, 0)
TolVt(8.2875, 16.85, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper' $end 'OperationIdentity' ParentOperationID=830
$end 'Operation' $end 'Operations' $end 'GeometryPart' $begin 'GeometryPart' $begin 'Attributes' Name='Rectangle40' Flags='' Color='(132 132 193)' Transparency=0
PartCoordinateSystem=1
UDMId=-1
MaterialValue='""' SolveInside=true
$end 'Attributes' $begin 'Operations' $begin 'Operation' OperationType='Rectangle' ID=859
ReferenceCoordSystemID=1
$begin 'RectangleParameters' KernelVersion=5
XStart='5.5mm' YStart='10.55mm' ZStart='1mm' Width='6.5mm' Height='0.5mm' WhichAxis='Z' $end 'RectangleParameters' ParentPartID=860
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=0
NumWires=1
NumLoops=0
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=860
StartFaceID=-1
StartEdgeID=861
StartVertexID=865
NumNewFaces=0
NumNewEdges=4
NumNewVertices=4
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$end 'OperationIdentity' $end 'Operation' $begin 'Operation' OperationType='CoverLines' ID=869
$begin 'LocalOperationParameters' KernelVersion=5
LocalOpPart=860
$end 'LocalOperationParameters' ParentPartID=860
IsSuppressed=false
$begin 'OperationIdentity' $begin 'Topology' NumLumps=1
NumShells=1
NumFaces=1
NumWires=0
NumLoops=1
NumCoedges=4
NumEdges=4
NumVertices=4
$end 'Topology' BodyID=-1
StartFaceID=870
StartEdgeID=-1
StartVertexID=-1
NumNewFaces=1
NumNewEdges=0
NumNewVertices=0
FaceNameAndIDMap()
EdgeNameAndIDMap()
VertexNameAndIDMap()
$begin
'GeomTopolBasedOperationIdentityHelper' $begin 'NewFaces' $begin 'Face' NormalizedSerialNum=0
ID=870
$begin 'FaceGeomTopol' FaceTopol(1, 4, 4, 4)
$begin
'FaceGeometry' Area=3.25
FcUVMid(8.75, 10.8, 1)
$begin
'FcTolVts' TolVt(5.5, 10.55, 1, 0)
TolVt(12, 10.55, 1, 0)
TolVt(12, 11.05, 1, 0)
TolVt(5.5, 11.05, 1, 0)
$end
'FcTolVts' $end
'FaceGeometry' $end 'FaceGeomTopol' $end 'Face' $end 'NewFaces' $begin 'NewEdges' $end 'NewEdges' $begin 'NewVertices' $end 'NewVertices' $end
'GeomTopolBasedOperationIdentityHelper'
$end 'OperationIdentity' ParentOperationID=859
$end 'Operation' $end 'Operations' $end 'GeometryPart' $end 'OperandParts' $begin 'Planes' $end 'Planes' $begin 'Points' $end 'Points' $begin 'GeometryEntityLists' $end 'GeometryEntityLists' $begin 'CachedNames' $begin 'allobjects' allobjects(-1)
$end 'allobjects' $begin 'global' global(-1)
$end 'global' $begin 'ground_plane' ground_plane(-1)
$end 'ground_plane' $begin 'radiation_box' radiation_box(-1)
$end 'radiation_box' $begin 'rectangle' rectangle(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41)
$end 'rectangle' $begin 'substrate' substrate(-1)
$end 'substrate' $end 'CachedNames' $end 'GeometryOperations' $begin 'GeometryDependencies' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 5)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 33)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 43)
DependencyObject('GeometryBodyOperation', 33)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 141)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 151)
DependencyObject('GeometryBodyOperation', 141)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=2
DependencyObject('GeometryBodyOperation', 694)
DependencyObject('GeometryBodyOperation', 151)
DependencyObject('GeometryBodyOperation', 407)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=2
DependencyObject('GeometryBodyOperation', 706)
DependencyObject('GeometryBodyOperation', 694)
DependencyObject('GeometryBodyOperation', 698)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=3
DependencyObject('GeometryBodyOperation', 842)
DependencyObject('GeometryBodyOperation', 706)
DependencyObject('GeometryBodyOperation', 804)
DependencyObject('GeometryBodyOperation', 709)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=3
DependencyObject('GeometryBodyOperation', 847)
DependencyObject('GeometryBodyOperation', 842)
DependencyObject('GeometryBodyOperation', 816)
DependencyObject('GeometryBodyOperation', 756)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=3
DependencyObject('GeometryBodyOperation', 852)
DependencyObject('GeometryBodyOperation', 847)
DependencyObject('GeometryBodyOperation', 840)
DependencyObject('GeometryBodyOperation', 780)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=5
DependencyObject('GeometryBodyOperation', 871)
DependencyObject('GeometryBodyOperation', 852)
DependencyObject('GeometryBodyOperation', 115)
DependencyObject('GeometryBodyOperation', 163)
DependencyObject('GeometryBodyOperation', 211)
DependencyObject('GeometryBodyOperation', 259)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=2
DependencyObject('GeometryBodyOperation', 880)
DependencyObject('GeometryBodyOperation', 871)
DependencyObject('GeometryBodyOperation', 869)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 885)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 895)
DependencyObject('GeometryBodyOperation', 885)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 925)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 93)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 103)
DependencyObject('GeometryBodyOperation', 93)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=2
DependencyObject('GeometryBodyOperation', 691)
DependencyObject('GeometryBodyOperation', 103)
DependencyObject('GeometryBodyOperation', 383)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=2
DependencyObject('GeometryBodyOperation', 697)
DependencyObject('GeometryBodyOperation', 691)
DependencyObject('GeometryBodyOperation', 419)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=5
DependencyObject('GeometryBodyOperation', 698)
DependencyObject('GeometryBodyOperation', 697)
DependencyObject('GeometryBodyOperation', 431)
DependencyObject('GeometryBodyOperation', 199)
DependencyObject('GeometryBodyOperation', 443)
DependencyObject('GeometryBodyOperation', 247)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 105)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 115)
DependencyObject('GeometryBodyOperation', 105)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 117)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 127)
DependencyObject('GeometryBodyOperation', 117)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=2
DependencyObject('GeometryBodyOperation', 740)
DependencyObject('GeometryBodyOperation', 127)
DependencyObject('GeometryBodyOperation', 539)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 129)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 139)
DependencyObject('GeometryBodyOperation', 129)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=2
DependencyObject('GeometryBodyOperation', 762)
DependencyObject('GeometryBodyOperation', 139)
DependencyObject('GeometryBodyOperation', 587)
$end 'DependencyInformation'
$begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 153)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 163)
DependencyObject('GeometryBodyOperation', 153)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 165)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 175)
DependencyObject('GeometryBodyOperation', 165)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 177)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 187)
DependencyObject('GeometryBodyOperation', 177)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 189)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 199)
DependencyObject('GeometryBodyOperation', 189)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 201)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 211)
DependencyObject('GeometryBodyOperation', 201)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 213)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 223)
DependencyObject('GeometryBodyOperation', 213)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=2
DependencyObject('GeometryBodyOperation', 746)
DependencyObject('GeometryBodyOperation', 223)
DependencyObject('GeometryBodyOperation', 563)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 225)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 235)
DependencyObject('GeometryBodyOperation', 225)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 237)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 247)
DependencyObject('GeometryBodyOperation', 237)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 249)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 259)
DependencyObject('GeometryBodyOperation', 249)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 261)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 271)
DependencyObject('GeometryBodyOperation', 261)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=2
DependencyObject('GeometryBodyOperation', 753)
DependencyObject('GeometryBodyOperation', 271)
DependencyObject('GeometryBodyOperation', 575)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 273)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 283)
DependencyObject('GeometryBodyOperation', 273)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=2
DependencyObject('GeometryBodyOperation', 771)
DependencyObject('GeometryBodyOperation', 283)
DependencyObject('GeometryBodyOperation', 623)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 373)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 383)
DependencyObject('GeometryBodyOperation', 373)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 397)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 407)
DependencyObject('GeometryBodyOperation', 397)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 409)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 419)
DependencyObject('GeometryBodyOperation', 409)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 421)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 431)
DependencyObject('GeometryBodyOperation', 421)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 433)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 443)
DependencyObject('GeometryBodyOperation', 433)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 445)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 455)
DependencyObject('GeometryBodyOperation', 445)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 457)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 467)
DependencyObject('GeometryBodyOperation', 457)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=5
DependencyObject('GeometryBodyOperation', 756)
DependencyObject('GeometryBodyOperation', 467)
DependencyObject('GeometryBodyOperation', 740)
DependencyObject('GeometryBodyOperation', 743)
DependencyObject('GeometryBodyOperation', 746)
DependencyObject('GeometryBodyOperation', 753)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 469)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 479)
DependencyObject('GeometryBodyOperation', 469)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=5
DependencyObject('GeometryBodyOperation', 780)
DependencyObject('GeometryBodyOperation', 479)
DependencyObject('GeometryBodyOperation', 762)
DependencyObject('GeometryBodyOperation', 765)
DependencyObject('GeometryBodyOperation', 768)
DependencyObject('GeometryBodyOperation', 771)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 481)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 491)
DependencyObject('GeometryBodyOperation', 481)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 493)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 503)
DependencyObject('GeometryBodyOperation', 493)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 505)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 515)
DependencyObject('GeometryBodyOperation', 505)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 517)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 527)
DependencyObject('GeometryBodyOperation', 517)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=5
DependencyObject('GeometryBodyOperation', 709)
DependencyObject('GeometryBodyOperation', 527)
DependencyObject('GeometryBodyOperation', 455)
DependencyObject('GeometryBodyOperation', 515)
DependencyObject('GeometryBodyOperation', 503)
DependencyObject('GeometryBodyOperation', 491)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 529)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 539)
DependencyObject('GeometryBodyOperation', 529)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 541)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 551)
DependencyObject('GeometryBodyOperation', 541)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=2
DependencyObject('GeometryBodyOperation', 743)
DependencyObject('GeometryBodyOperation', 551)
DependencyObject('GeometryBodyOperation', 175)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 553)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 563)
DependencyObject('GeometryBodyOperation', 553)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 565)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 575)
DependencyObject('GeometryBodyOperation', 565)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 577)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 587)
DependencyObject('GeometryBodyOperation', 577)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 589)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 599)
DependencyObject('GeometryBodyOperation', 589)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=2
DependencyObject('GeometryBodyOperation', 765)
DependencyObject('GeometryBodyOperation', 599)
DependencyObject('GeometryBodyOperation', 187)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 601)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 611)
DependencyObject('GeometryBodyOperation', 601)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=2
DependencyObject('GeometryBodyOperation', 768)
DependencyObject('GeometryBodyOperation', 611)
DependencyObject('GeometryBodyOperation', 235)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 613)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 623)
DependencyObject('GeometryBodyOperation', 613)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 794)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 804)
DependencyObject('GeometryBodyOperation', 794)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 806)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 816)
DependencyObject('GeometryBodyOperation', 806)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 830)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 840)
DependencyObject('GeometryBodyOperation', 830)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 859)
DependencyObject('CoordinateSystem', 1)
$end 'DependencyInformation' $begin 'DependencyInformation' NumParents=1
DependencyObject('GeometryBodyOperation', 869)
DependencyObject('GeometryBodyOperation', 859)
$end 'DependencyInformation' $end 'GeometryDependencies' $end 'GeometryCore' GroupByMaterial('-1'=true)
GroupSheetByMaterial()
$begin 'LastUserInputs' $end 'LastUserInputs' $end 'ModelSetup' $begin 'BoundarySetup' $begin 'GlobalBoundData' PortImpedance='1' GlobalMaterialEnv='vacuum' $end 'GlobalBoundData' $begin 'Boundaries' NextUniqueID=5
MoveBackwards=false
$begin 'PerfE1' ID=1
BoundType='Perfect E' Objects(34)
ParentBndID=-1
InfGroundPlane=false
$end 'PerfE1' $begin 'PerfE2' ID=2
BoundType='Perfect E' Objects(142)
ParentBndID=-1
InfGroundPlane=false
$end 'PerfE2' $begin 'Rad1' ID=4
BoundType='Radiation' Objects(926)
ParentBndID=-1
IsIncidentField=false
IsEnforcedField=false
IsFssReference=false
IsForPML=false
UseAdaptiveIE=false
IncludeInPostproc=true
$end 'Rad1' $begin '1' ID=0
BoundType='Lumped Port' Objects(886)
ParentBndID=-1
RenormalizeAllTerminals=true
DoDeembed=false
$begin 'Modes' $begin 'Mode1' ModeNum=1
UseIntLine=true
$begin 'IntLine' $begin 'GeometryPosition' IsAttachedToEntity=true
EntityID=890
PositionType='EdgeCenter' UParam=0
VParam=0
XPosition='0' YPosition='0' ZPosition='0' $end 'GeometryPosition' $begin 'GeometryPosition' IsAttachedToEntity=true
EntityID=891
PositionType='OnVertex' UParam=0
VParam=0
XPosition='0' YPosition='0' ZPosition='0' $end 'GeometryPosition' $end 'IntLine' CharImp='Zpi' AlignmentGroup=0
RenormImp='50ohm'
$end 'Mode1' $end 'Modes' ShowReporterFilter=false
ReporterFilter(true)
FullResistance='50ohm' FullReactance='0ohm' $end '1' $end 'Boundaries' $begin 'ProductSpecificData' $begin 'PMLData' $begin 'PMLGroups' $end 'PMLGroups' $end 'PMLData' $begin 'SortOrder' Port[1: -1]
Terminal[1: -1]
$end 'SortOrder' $end 'ProductSpecificData' $end 'BoundarySetup' $begin 'ArrayDefinition' NextUniqueID=0
MoveBackwards=false
$end 'ArrayDefinition' $begin 'MeshSetup' $begin 'MeshSettings' $begin 'GlobalSurfApproximation' SurfDevChoice=0
NormalDevChoice=1
AspectRatioChoice=1
PullToTrueSurf=false
SetFacePreservationLevel=0
$end 'GlobalSurfApproximation' MeshMethod='Auto' $end 'MeshSettings' $begin 'MeshOperations' NextUniqueID=0
MoveBackwards=false
$end 'MeshOperations' $end 'MeshSetup' $begin 'AnalysisSetup' $begin 'HfssGlobalData' NextUniqueID=0
MoveBackwards=false
$end 'HfssGlobalData' $begin 'SolveSetups' NextUniqueID=1
MoveBackwards=false
$begin 'Setup1' ID=0
SetupType='HfssDriven' Frequency='12GHz' PortsOnly=false
MaxDeltaS=0.02
UseMatrixConv=false
MaximumPasses=6
MinimumPasses=1
MinimumConvergedPasses=1
PercentRefinement=30
IsEnabled=true
BasisOrder=1
UseIterativeSolver=false
DoLambdaRefine=true
DoMaterialLambda=true
SetLambdaTarget=false
Target=0.3333
UseMaxTetIncrease=false
PortAccuracy=2
UseABCOnPort=false
SetPortMinMaxTri=false
PortMinTri=100
PortMaxTri=500
EnableSolverDomains=false
SaveRadFieldsOnly=false
SaveAnyFields=true
NoAdditionalRefinementOnImport=false
$begin 'Sweeps' NextUniqueID=1
MoveBackwards=false
$begin 'Sweep' ID=0
IsEnabled=true
SetupType='LinearStep' StartValue='1GHz' StopValue='15GHz' StepSize='0.1GHz' Type='Fast' SaveFields=true
SaveRadFields=false
GenerateFieldsForAllFreqs=false
ExtrapToDC=false
$end 'Sweep' $end 'Sweeps' DerivativesOnlyForLastPass=false
$end 'Setup1' $end 'SolveSetups' $end 'AnalysisSetup' $begin 'Optimetrics' $begin 'OptimetricsSetups'
NextUniqueID=0
MoveBackwards=false
$end 'OptimetricsSetups' $end 'Optimetrics' $begin 'Solutions' FieldType='NoIncidentWave' IncludePortPostProcessing=false
SourceEntry(ID=0, Index=0, Terminal=false, Terminated=false, Magnitude='1W', Phase='0deg')
$begin 'Contexts' NextUniqueID=1
MoveBackwards=false
$end 'Contexts' $end 'Solutions' $begin 'PortFieldDisplay' $begin 'PortFieldDisplay' ScaleFactor=5
Solution='Setup1 : LastAdaptive' Frequency='12GHz' $end 'PortFieldDisplay' $end 'PortFieldDisplay' $begin 'FieldsReporter' $begin 'FieldsCalculator' Line_Discretization=1000
$end 'FieldsCalculator' $begin 'PlotDefaults' Default_SolutionId=266
Default_PlotFolder='Automatic' Default_Phase='0deg' Default_Freq='12GHz' $end 'PlotDefaults' $begin 'FieldsPlotManagerID' NextUniqueID=0
MoveBackwards=false
NumQuantityType=0
NumPlots=0
$end 'FieldsPlotManagerID' $begin 'Report3dInGeomWnd' Report3dNum=3
$begin 'Report3dPlot_1' ReportID=9
Transparency=0
ScaleFactor=0.5
Visible=false
CoordSys=-1
$end 'Report3dPlot_1' $begin 'Report3dPlot_2' ReportID=11
Transparency=0
ScaleFactor=0.5
Visible=false
CoordSys=-1
$end 'Report3dPlot_2' $begin 'Report3dPlot_3' ReportID=17
Transparency=0
ScaleFactor=0.5
Visible=false
CoordSys=-1
$end 'Report3dPlot_3' $end 'Report3dInGeomWnd' $end 'FieldsReporter' $begin 'RadField' $begin 'FarFieldSetups' NextUniqueID=3
MoveBackwards=false
$begin 'Infinite Sphere1' Type='Infinite Sphere' ID=0
VersionID=2
UseCustomRadiationSurface=false
ThetaStart='-180deg' ThetaStop='180deg' ThetaStep='10deg' PhiStart='0deg' PhiStop='360deg' PhiStep='10deg' UseLocalCS=false
$end 'Infinite Sphere1' $end 'FarFieldSetups' $begin 'ArraySetup' UseOption='NoArray' $begin 'RegularArray' NumUCells='10' NumVCells='10' CellUDist='10mm' CellVDist='10mm' UDirnX='1' UDirnY='0' UDirnZ='0' VDirnX='0' VDirnY='1' VDirnZ='0' FirstCellPosX='0mm' FirstCellPosY='0mm' FirstCellPosZ='0mm' Behavior='UseSlaveSettings' ScanAnglePhi='45deg'
ScanAngleTheta='45deg' UDirnPhaseShift='0deg' VDirnPhaseShift='0deg' $end 'RegularArray' $begin 'CustomArray' NumCells=0
$begin 'Cell' $end 'Cell' $end 'CustomArray' $end 'ArraySetup' $begin 'NearFieldSetups' NextUniqueID=3
MoveBackwards=false
$end 'NearFieldSetups' RadFieldComputationVersion=1.4
RadfieldHeaderFile='RADC2A342016397559701.tmp' $end 'RadField' $begin 'SolutionManager' $begin 'SimSetup' TypeName='BaseSetup' ID=264
Name='Setup1' $begin 'Solution' ID=265
Name='AdaptivePass' $begin 'SimDataExtractor' $begin 'Sweeps' $begin 'Sweep' Variable='Pass' Column='1;2;3;4;5;6' Units='' $end 'Sweep' $begin 'Sweep' Variable='Freq' Column='12GHz' Units='GHz' $end 'Sweep' $begin 'PostprocessSweep' Variable='NormalizedDistance' RegularSweep=1
Units='' Minimum=0
Maximum=1
Increment=0.01
CreateIndexedSubsweepFlag=false
$end 'PostprocessSweep' $begin 'PostprocessSweep' Variable='Phi' RegularSweep=1
Units='deg' Minimum=0
Maximum=6.28318530717959
Increment=0.0872664625997165
CreateIndexedSubsweepFlag=false
$end 'PostprocessSweep' $begin 'PostprocessSweep' Variable='Theta' RegularSweep=1
Units='deg' Minimum=0
Maximum=6.28318530717959
Increment=0.0872664625997165
CreateIndexedSubsweepFlag=false
$end 'PostprocessSweep' $begin 'PostprocessSweep' Variable='Phase' RegularSweep=1
Units='deg' Minimum=0
Maximum=6.28318530717959
Increment=0.0872664625997165
CreateIndexedSubsweepFlag=false
$end 'PostprocessSweep' $end 'Sweeps' IsPortOnly=false
$end 'SimDataExtractor' $end 'Solution' $begin 'Solution' ID=266
Name='LastAdaptive' $begin 'SimDataExtractor' SimValue('rETotal', 1, 67, false, SimValueID=326, 0, 0, 2, 0, false, false, 0, 1, 0, 1, 1, '', 0, 0)
SimValue('GainTotal', 1, 90, true, SimValueID=327, 0, 0, 2, 0, false, false, 0, 1, 0, 1, 1, '', 0, 0)
SimValue('DirTotal', 1, 90, true, SimValueID=328, 0, 0, 2, 0, false, false, 0, 1, 0, 1, 1, '', 0, 0)
SimValue('Sphere1meter', 1, 90, false, SimValueID=334, 3, 0, 2, 0, false, false, -1, 1, 0, 1, 1, '', 0, 0)
$begin 'Sweeps' $begin 'Sweep' Variable='Freq' Column='12GHz' Units='GHz' $end 'Sweep' $begin 'PostprocessSweep' Variable='NormalizedDistance' RegularSweep=1
Units='' Minimum=0
Maximum=1
Increment=0.01
CreateIndexedSubsweepFlag=false
$end 'PostprocessSweep' $begin 'PostprocessSweep' Variable='Phi' RegularSweep=1
Units='deg' Minimum=0
Maximum=6.28318530717959
Increment=0.0872664625997165
CreateIndexedSubsweepFlag=false
$end 'PostprocessSweep' $begin 'PostprocessSweep' Variable='Theta' RegularSweep=1
Units='deg' Minimum=0
Maximum=6.28318530717959
Increment=0.0872664625997165
CreateIndexedSubsweepFlag=false
$end 'PostprocessSweep' $begin 'PostprocessSweep' Variable='Phase' RegularSweep=1
Units='deg' Minimum=0
Maximum=6.28318530717959
Increment=0.0872664625997165
CreateIndexedSubsweepFlag=false
$end 'PostprocessSweep' $end 'Sweeps' IsPortOnly=false
$end 'SimDataExtractor' $end 'Solution' $begin 'Solution' ID=267
Name='Sweep' $begin 'SimDataExtractor' SimValue('DirTotal', 1, 90, true, SimValueID=329, 0, 0, 2, 0, false, false, 0, 1, 0, 1, 1, '', 0, 0)
SimValue('S(1,1)', 2, 90, false, SimValueID=331, 3, 0, 2, 0, false, false, -1, 1, 0, 1, 1, '', 0, 0)
SimValue('VSWR(1)', 1, 90, false, SimValueID=332, 3, 0, 2, 0, false, false, -1, 1, 0, 1, 1, '', 0, 0)
SimValue('S(1,1)', 2, 90, false, SimValueID=333, 0, 0, 2, 0, false, false, -1, 1, 0, 1, 1, '', 0, 0)
$begin 'Sweeps' $begin 'PostprocessSweep' Variable='Freq' RegularSweep=1
Units='GHz' Minimum=1000000000
Maximum=15000000000
Increment=100000000
CreateIndexedSubsweepFlag=false
$end 'PostprocessSweep' $begin 'PostprocessSweep' Variable='NormalizedDistance' RegularSweep=1
Units='' Minimum=0
Maximum=1
Increment=0.01
CreateIndexedSubsweepFlag=false
$end 'PostprocessSweep' $begin 'PostprocessSweep' Variable='Phi' RegularSweep=1
Units='deg' Minimum=0
Maximum=6.28318530717959
Increment=0.0872664625997165
CreateIndexedSubsweepFlag=false
$end 'PostprocessSweep' $begin 'PostprocessSweep' Variable='Theta' RegularSweep=1
Units='deg' Minimum=0
Maximum=6.28318530717959
Increment=0.0872664625997165
CreateIndexedSubsweepFlag=false
$end 'PostprocessSweep' $begin 'PostprocessSweep' Variable='Phase' RegularSweep=1
Units='deg' Minimum=0
Maximum=6.28318530717959
Increment=0.0872664625997165
CreateIndexedSubsweepFlag=false
$end 'PostprocessSweep' $end 'Sweeps' IsPortOnly=false
$end 'SimDataExtractor'
$end 'Solution' $end 'SimSetup' $begin 'Version ID Map' V=260
$begin 'Setup' N='Setup1' V=0
Soln(N='AdaptivePass', V=0)
Soln(N='LastAdaptive', V=0)
Soln(N='Sweep', V=0)
$end 'Setup' $end 'Version ID Map' $begin 'ID Map' $begin 'Setup' N='Setup1' I=264
Soln(N='AdaptivePass', I=265)
Soln(N='LastAdaptive', I=266)
Soln(N='Sweep', I=267)
$end 'Setup' $end 'ID Map' $end 'SolutionManager' $begin 'UserDefinedSolutionMgr' NextUniqueID=1000000
MoveBackwards=false
$end 'UserDefinedSolutionMgr' $begin 'DatasetSolutionMgr' NextUniqueID=2000000
MoveBackwards=false
$end 'DatasetSolutionMgr' Notes=$begin_cdata$ $end_cdata$
$begin 'AnimationSetups' $end 'AnimationSetups' CacheHeaderFile='HDR4E4A3420163976115417.tmp' $end 'HFSSModel' $begin 'DataInstances' $begin 'Instance' DesignEditor='HFSSDesign1' $begin 'HfssDesignInstance' DesignInstanceID=1
$begin 'WindowPosition' $begin 'EditorWindow'
'3D Modeler'(Editor3d(View(WindowPos(5, -1, -1, -8, -31, 0, 0, 920, 409), OrientationMatrix(0.0323536060750484, -0.108592756092548, 0.0227134227752686, 0, 0.110417045652866, 0.0338249243795872, 0.00444926042109728, 0, -0.0108292130753398, 0.0204555075615644, 0.113223649561405, 0, -1.82969200611115, 0.0478053987026215, -
5.77095174789429, 1, 0, -3.26105093955994, 2.19598507881165, -1.64158797264099, 1.1954505443573, -3.67763137817383, 14.9249668121338), Drawings[5: 'Substrate', 'Ground_Plane',
'Rectangle5', 'Rectangle41', 'Radiation_box'], 'View Data'('Render Mode'=1, 'Show Ruler'=1),
ClipPlanes(ClipPlaneOptions(DisableWhenDrawingNewPlane=true, ForceOpqaueForUnclipped=false, ShowClipped=false, Transparency=0, HandleColor=16776960)))))
$end 'EditorWindow' $end 'WindowPosition' $begin 'ReportSetup' $begin 'ReportManager' $begin 'Reports' $begin 'Return Loss' ReportID=5
ReportName='Return Loss' $begin 'TraceDef' TraceDefinitionType='TraceDefinition' $begin 'DesignSolnDefn' $begin
'DESIGN_SOLUTION_SIM_VALUE_CONTEXT' DesignID=0
SolutionID=267
$begin
'REPORT_TYPE_SIM_VALUE_CONTEXT' ReportType=0
SimValueContext(3, 0, 2, 0, false, false, -1, 1, 0, 1, 1, '', 0, 0)
$end
'REPORT_TYPE_SIM_VALUE_CONTEXT' $end
'DESIGN_SOLUTION_SIM_VALUE_CONTEXT' $end 'DesignSolnDefn' ID=4
VersionID=5
Name='dB(S(1,1))' TieNameToExpr=true
$begin 'Components' $begin 'TraceComponentDefinition' Expr='Freq' $end 'TraceComponentDefinition' $begin 'TraceComponentDefinition' Expr='dB(S(1,1))' $end 'TraceComponentDefinition' $end 'Components' $begin 'ExtendedTraceInfo' NumPoints=0
TraceType=0
Offset=0
XLabel='' SamplingPeriod='0' SamplingPeriodOffset='0' AutoDelay=true
DelayValue='0ps' AutoCompCrossAmplitude=true
CrossingAmplitude='0mV' YAxis=1
AutoCompEyeMeasurementPoint=true
EyeMeasurementPoint='0ps' $end 'ExtendedTraceInfo' $begin 'TraceFamiliesDisplayDefinition' DisplayFamiliesType='DisplayAll' $end 'TraceFamiliesDisplayDefinition' $begin 'PointsetDefinition' $begin 'SubsweepDefParamsContainer' $begin '0' SubsweepType='Specifiable' SubsweepChoiceType='All' SweepVariableName='Freq' $end '0' $end 'SubsweepDefParamsContainer' FamilyBlock()
$end 'PointsetDefinition' DesignInstanceID=1
$end 'TraceDef' $end 'Return Loss' $begin 'VSWR' ReportID=7
ReportName='VSWR' $begin 'TraceDef' TraceDefinitionType='TraceDefinition' $begin 'DesignSolnDefn' $begin
'DESIGN_SOLUTION_SIM_VALUE_CONTEXT' DesignID=0
SolutionID=267
$begin
'REPORT_TYPE_SIM_VALUE_CONTEXT' ReportType=0
SimValueContext(3, 0, 2, 0, false, false, -1, 1, 0, 1, 1, '', 0, 0)
$end
'REPORT_TYPE_SIM_VALUE_CONTEXT' $end
'DESIGN_SOLUTION_SIM_VALUE_CONTEXT' $end 'DesignSolnDefn' ID=6
VersionID=7
Name='dB(VSWR(1))' TieNameToExpr=true
$begin 'Components' $begin 'TraceComponentDefinition' Expr='Freq' $end 'TraceComponentDefinition'
$begin 'TraceComponentDefinition' Expr='dB(VSWR(1))' $end 'TraceComponentDefinition' $end 'Components' $begin 'ExtendedTraceInfo' NumPoints=0
TraceType=0
Offset=0
XLabel='' SamplingPeriod='0' SamplingPeriodOffset='0' AutoDelay=true
DelayValue='0ps' AutoCompCrossAmplitude=true
CrossingAmplitude='0mV' YAxis=1
AutoCompEyeMeasurementPoint=true
EyeMeasurementPoint='0ps' $end 'ExtendedTraceInfo' $begin 'TraceFamiliesDisplayDefinition' DisplayFamiliesType='DisplayAll' $end 'TraceFamiliesDisplayDefinition' $begin 'PointsetDefinition' $begin 'SubsweepDefParamsContainer' $begin '0' SubsweepType='Specifiable' SubsweepChoiceType='All' SweepVariableName='Freq' $end '0' $end 'SubsweepDefParamsContainer' FamilyBlock()
$end 'PointsetDefinition' DesignInstanceID=1
$end 'TraceDef' $end 'VSWR' $begin '3D Polar Plot 1' ReportID=9
ReportName='3D Polar Plot 1' $begin 'TraceDef' TraceDefinitionType='TraceDefinition' $begin 'DesignSolnDefn' $begin
'DESIGN_SOLUTION_SIM_VALUE_CONTEXT' DesignID=0
SolutionID=266
$begin
'REPORT_TYPE_SIM_VALUE_CONTEXT' ReportType=3
SimValueContext(0, 0, 2, 0, false, false, 0, 1, 0, 1, 1, '', 0, 0)
$end
'REPORT_TYPE_SIM_VALUE_CONTEXT' $end
'DESIGN_SOLUTION_SIM_VALUE_CONTEXT' $end 'DesignSolnDefn' ID=8
VersionID=9
Name='dB(GainTotal)' TieNameToExpr=true
$begin 'Components' $begin 'TraceComponentDefinition' Expr='Phi' $end 'TraceComponentDefinition' $begin 'TraceComponentDefinition' Expr='Theta' $end 'TraceComponentDefinition' $begin 'TraceComponentDefinition' Expr='dB(GainTotal)' $end 'TraceComponentDefinition' $end 'Components' $begin 'ExtendedTraceInfo' NumPoints=0
TraceType=0
Offset=0
XLabel='' SamplingPeriod='0' SamplingPeriodOffset='0' AutoDelay=true
DelayValue='0ps' AutoCompCrossAmplitude=true
CrossingAmplitude='0mV' YAxis=1
AutoCompEyeMeasurementPoint=true
EyeMeasurementPoint='0ps' $end 'ExtendedTraceInfo' $begin 'TraceFamiliesDisplayDefinition' DisplayFamiliesType='DisplayAll' $end 'TraceFamiliesDisplayDefinition' $begin 'PointsetDefinition' $begin 'SubsweepDefParamsContainer' $begin '0' SubsweepType='Regular' SubsweepChoiceType='All' SweepVariableName='Phi' $end '0' $begin '1' SubsweepType='Regular'
SubsweepChoiceType='All' SweepVariableName='Theta' $end '1' $begin '2' SubsweepType='Regular' SubsweepChoiceType='Selected' SweepVariableName='Freq' ColumnValues(12000000000)
ParameterType='DoubleParam' Units='GHz' $end '2' $end 'SubsweepDefParamsContainer' FamilyBlock()
$end 'PointsetDefinition' DesignInstanceID=1
$end 'TraceDef' $end '3D Polar Plot 1' $begin '3D Polar Plot 2' ReportID=11
ReportName='3D Polar Plot 2' $begin 'TraceDef' TraceDefinitionType='TraceDefinition' $begin 'DesignSolnDefn' $begin
'DESIGN_SOLUTION_SIM_VALUE_CONTEXT' DesignID=0
SolutionID=266
$begin
'REPORT_TYPE_SIM_VALUE_CONTEXT' ReportType=3
SimValueContext(0, 0, 2, 0, false, false, 0, 1, 0, 1, 1, '', 0, 0)
$end
'REPORT_TYPE_SIM_VALUE_CONTEXT' $end
'DESIGN_SOLUTION_SIM_VALUE_CONTEXT' $end 'DesignSolnDefn' ID=10
VersionID=11
Name='dB(rETotal)' TieNameToExpr=true
$begin 'Components' $begin 'TraceComponentDefinition' Expr='Phi' $end 'TraceComponentDefinition' $begin 'TraceComponentDefinition' Expr='Theta' $end 'TraceComponentDefinition' $begin 'TraceComponentDefinition'
Expr='dB(rETotal)' $end 'TraceComponentDefinition' $end 'Components' $begin 'ExtendedTraceInfo' NumPoints=0
TraceType=0
Offset=0
XLabel='' SamplingPeriod='0' SamplingPeriodOffset='0' AutoDelay=true
DelayValue='0ps' AutoCompCrossAmplitude=true
CrossingAmplitude='0mV' YAxis=1
AutoCompEyeMeasurementPoint=true
EyeMeasurementPoint='0ps' $end 'ExtendedTraceInfo' $begin 'TraceFamiliesDisplayDefinition' DisplayFamiliesType='DisplayAll' $end 'TraceFamiliesDisplayDefinition' $begin 'PointsetDefinition' $begin 'SubsweepDefParamsContainer' $begin '0' SubsweepType='Regular' SubsweepChoiceType='All' SweepVariableName='Phi' $end '0' $begin '1' SubsweepType='Regular' SubsweepChoiceType='All' SweepVariableName='Theta' $end '1' $begin '2' SubsweepType='Regular' SubsweepChoiceType='Selected' SweepVariableName='Freq' ColumnValues(12000000000)
ParameterType='DoubleParam' Units='GHz' $end '2' $end 'SubsweepDefParamsContainer' FamilyBlock()
$end 'PointsetDefinition' DesignInstanceID=1
$end 'TraceDef' $end '3D Polar Plot 2' $begin 'XY Plot 1' ReportID=13
ReportName='XY Plot 1' $begin 'TraceDef' TraceDefinitionType='TraceDefinition' $begin 'DesignSolnDefn' $begin
'DESIGN_SOLUTION_SIM_VALUE_CONTEXT' DesignID=0
SolutionID=266
$begin
'REPORT_TYPE_SIM_VALUE_CONTEXT' ReportType=3
SimValueContext(0, 0, 2, 0, false, false, 0, 1, 0, 1, 1, '', 0, 0)
$end
'REPORT_TYPE_SIM_VALUE_CONTEXT' $end
'DESIGN_SOLUTION_SIM_VALUE_CONTEXT' $end 'DesignSolnDefn' ID=12
VersionID=13
Name='dB(rETotal)' TieNameToExpr=true
$begin 'Components' $begin 'TraceComponentDefinition' Expr='Theta' $end 'TraceComponentDefinition' $begin 'TraceComponentDefinition' Expr='dB(rETotal)' $end 'TraceComponentDefinition' $end 'Components' $begin 'ExtendedTraceInfo' NumPoints=0
TraceType=0
Offset=0
XLabel='' SamplingPeriod='0' SamplingPeriodOffset='0' AutoDelay=true
DelayValue='0ps' AutoCompCrossAmplitude=true
CrossingAmplitude='0mV' YAxis=1
AutoCompEyeMeasurementPoint=true
EyeMeasurementPoint='0ps' $end 'ExtendedTraceInfo' $begin 'TraceFamiliesDisplayDefinition' DisplayFamiliesType='DisplayAll' $end 'TraceFamiliesDisplayDefinition' $begin 'PointsetDefinition'
$begin 'SubsweepDefParamsContainer' $begin '0' SubsweepType='Regular' SubsweepChoiceType='All' SweepVariableName='Theta' $end '0' $begin '1' SubsweepType='Regular' SubsweepChoiceType='All' SweepVariableName='Phi' $end '1' $begin '2' SubsweepType='Regular' SubsweepChoiceType='Selected' SweepVariableName='Freq' ColumnValues(12000000000)
ParameterType='DoubleParam' Units='GHz' $end '2' $end 'SubsweepDefParamsContainer' FamilyBlock()
$end 'PointsetDefinition' DesignInstanceID=1
$end 'TraceDef' $end 'XY Plot 1' $begin 'Radiation Pattern 1' ReportID=15
ReportName='Radiation Pattern 1' $begin 'TraceDef' TraceDefinitionType='TraceDefinition' $begin 'DesignSolnDefn' $begin
'DESIGN_SOLUTION_SIM_VALUE_CONTEXT' DesignID=0
SolutionID=266
$begin
'REPORT_TYPE_SIM_VALUE_CONTEXT' ReportType=3
SimValueContext(0, 0, 2, 0, false, false, 0, 1, 0, 1, 1, '', 0, 0)
$end
'REPORT_TYPE_SIM_VALUE_CONTEXT' $end
'DESIGN_SOLUTION_SIM_VALUE_CONTEXT' $end 'DesignSolnDefn' ID=14
VersionID=15
Name='dB(rETotal)' TieNameToExpr=true
$begin 'Components' $begin 'TraceComponentDefinition' Expr='Theta' $end 'TraceComponentDefinition' $begin 'TraceComponentDefinition' Expr='dB(rETotal)' $end 'TraceComponentDefinition' $end 'Components' $begin 'ExtendedTraceInfo' NumPoints=0
TraceType=0
Offset=0
XLabel='' SamplingPeriod='0' SamplingPeriodOffset='0' AutoDelay=true
DelayValue='0ps' AutoCompCrossAmplitude=true
CrossingAmplitude='0mV' YAxis=1
AutoCompEyeMeasurementPoint=true
EyeMeasurementPoint='0ps' $end 'ExtendedTraceInfo' $begin 'TraceFamiliesDisplayDefinition' DisplayFamiliesType='DisplayAll' $end 'TraceFamiliesDisplayDefinition' $begin 'PointsetDefinition' $begin 'SubsweepDefParamsContainer' $begin '0' SubsweepType='Regular' SubsweepChoiceType='All' SweepVariableName='Theta' $end '0' $begin '1' SubsweepType='Regular' SubsweepChoiceType='All' SweepVariableName='Phi' $end '1' $begin '2' SubsweepType='Regular' SubsweepChoiceType='Selected' SweepVariableName='Freq' ColumnValues(12000000000)
ParameterType='DoubleParam' Units='GHz' $end '2' $end 'SubsweepDefParamsContainer' FamilyBlock()
$end 'PointsetDefinition'
DesignInstanceID=1
$end 'TraceDef' $end 'Radiation Pattern 1' $begin '3D Polar Plot 3' ReportID=17
ReportName='3D Polar Plot 3' $begin 'TraceDef' TraceDefinitionType='TraceDefinition' $begin 'DesignSolnDefn' $begin
'DESIGN_SOLUTION_SIM_VALUE_CONTEXT' DesignID=0
SolutionID=266
$begin
'REPORT_TYPE_SIM_VALUE_CONTEXT' ReportType=3
SimValueContext(0, 0, 2, 0, false, false, 0, 1, 0, 1, 1, '', 0, 0)
$end
'REPORT_TYPE_SIM_VALUE_CONTEXT' $end
'DESIGN_SOLUTION_SIM_VALUE_CONTEXT' $end 'DesignSolnDefn' ID=16
VersionID=17
Name='dB(DirTotal)' TieNameToExpr=true
$begin 'Components' $begin 'TraceComponentDefinition' Expr='Phi' $end 'TraceComponentDefinition' $begin 'TraceComponentDefinition' Expr='Theta' $end 'TraceComponentDefinition' $begin 'TraceComponentDefinition' Expr='dB(DirTotal)' $end 'TraceComponentDefinition' $end 'Components' $begin 'ExtendedTraceInfo' NumPoints=0
TraceType=0
Offset=0
XLabel='' SamplingPeriod='0' SamplingPeriodOffset='0' AutoDelay=true
DelayValue='0ps' AutoCompCrossAmplitude=true
CrossingAmplitude='0mV'
YAxis=1
AutoCompEyeMeasurementPoint=true
EyeMeasurementPoint='0ps' $end 'ExtendedTraceInfo' $begin 'TraceFamiliesDisplayDefinition' DisplayFamiliesType='DisplayAll' $end 'TraceFamiliesDisplayDefinition' $begin 'PointsetDefinition' $begin 'SubsweepDefParamsContainer' $begin '0' SubsweepType='Regular' SubsweepChoiceType='All' SweepVariableName='Phi' $end '0' $begin '1' SubsweepType='Regular' SubsweepChoiceType='All' SweepVariableName='Theta' $end '1' $begin '2' SubsweepType='Regular' SubsweepChoiceType='Selected' SweepVariableName='Freq' ColumnValues(12000000000)
ParameterType='DoubleParam' Units='GHz' $end '2' $end 'SubsweepDefParamsContainer' FamilyBlock()
$end 'PointsetDefinition' DesignInstanceID=1
$end 'TraceDef' $end '3D Polar Plot 3' $end 'Reports' NextUniqueID=18
MoveBackwards=false
$begin 'NextVersID' NextUniqueID=18
MoveBackwards=false
$end 'NextVersID' $end 'ReportManager' $begin 'Reports' $begin 'Return Loss' ReportID=5
$begin 'Report2D' name='Return Loss' ReportID=5
ReportType=0
DisplayType=1
Title='' Domain='' $begin 'Graph2DsV2' $begin 'Graph2D' TraceDefID=4
Type='Continuous' Axis='Y1' $end 'Graph2D' $end 'Graph2DsV2' $begin 'PlotDisplayDataManager' NextUniqueID=27
MoveBackwards=false
$begin 'PlotHeaderDataSource' CompanyName='' ShowDesignName=true
ProjectFileName='' $end 'PlotHeaderDataSource' StockNameIDMap(AxisX=1, AxisY1=2, AxisY2=8, AxisY3=9, AxisY4=10, Grid=11, Header=0, Legend=5, MarkerLegend=25, XYHorizScroller=7)
$begin 'SourceList' $begin 'ListItem' $begin 'MarkerDataSource' MarkerID=23
MarkerName='m1' AttachedToDrawing=true
CurveID=21
CurveDefinition='Cartesian' PrimarySweepValue='9.7GHz' $end 'MarkerDataSource' $end 'ListItem' $end 'SourceList' $begin 'DocAttributes' $begin 'PlotAttributeStoreMap' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=11
$begin
'CartesianGridDescAttribute' ShowXMinor=true
ShowYMinor=true
ShowXMajor=true
ShowYMajor=true
ShowBorder=true
$end
'CartesianGridDescAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem'
DataSourceID=21
$begin
'CurveCartesianAttribute' YAxis='Y1' $end
'CurveCartesianAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=21
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=255, G=0, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HorizontalLeftTriangle' SymbolColor(R=0, G=25, B=185)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=0
$begin
'HeaderRenderAttribute' $begin 'TitleFont' $begin
'FontAttribute' $begin
'Font' Height=-19
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'TitleFont' $begin 'SubtitleFont' $begin
'FontAttribute' $begin
'Font' Height=-13
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'SubtitleFont' $end
'HeaderRenderAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=5
$begin
'LegendRenderAttribute' $begin
'LegendTableAttrib' $begin
'TableRenderAttribute' $begin
'TableFontAttrib' $begin 'FontAttribute' $begin 'Font' Height=-11
Width=0
Escapement=0 Orientation=0 Weight=400 Italic=0 Underline=0 StrikeOut=0 CharSet=0 OutPrecision=7 ClipPrecision=48 Quality=6 PitchAndFamily=0 FaceName='Arial' $end 'Font' Color(R=0, G=0, B=0) $end 'FontAttribute' $end 'TableFontAttrib' $begin 'TableTitleFontAttrib' $begin 'FontAttribute' $begin 'Font' Height=-11 Width=0 Escapement=0 Orientation=0 Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end 'Font' Color(R=0, G=0, B=0)
$end 'FontAttribute' $end
'TableTitleFontAttrib' TableBorderLineWidth=1
TableBorderLineColor=0
TableGridLineWidth=1
TableGridLineColor=12632256
TableBackgroundColor=16777215
TableHeaderBackgroundColor=14408667
$end
'TableRenderAttribute' $end
'LegendTableAttrib' ShowTraceName=true
ShowSolutionName=true
ShowVariationKey=true
DockMode='None'
$end
'LegendRenderAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=1
$begin
'LineAxisRenderAttribute' DecimalFieldWidth=3
DecimalFieldPrecision=2
ManualTitle='' AxisColor(R=0, G=0, B=0)
MinScale=0
MaxScale=1
TickSpacing=1
ManualUnits=false
Units='mm' AxisScale='Linear' NumberFormat='Auto' $begin 'TextFont' $begin
'FontAttribute' $begin
'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'TextFont' InfMapMode=false
InfMapValue=1.79769313486232e+306
AutoRangeMin=true
AutoRangeMax=true
AutoSpacing=true
kNumMinorDivisions=5
ShowAxisTitle=true
ShowAxisUnits=true
vwm='FullWnd' viewWndWd=#nan
ActivateMargins=true
MarginPercent=0
$end
'LineAxisRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=2
$begin
'LineAxisRenderAttribute' DecimalFieldWidth=3
DecimalFieldPrecision=2
ManualTitle='' AxisColor(R=0, G=0, B=0)
MinScale=0
MaxScale=1
TickSpacing=1
ManualUnits=false
Units='mm'
AxisScale='Linear' NumberFormat='Auto' $begin 'TextFont' $begin
'FontAttribute' $begin
'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'TextFont' InfMapMode=false
InfMapValue=1.79769313486232e+306
AutoRangeMin=true
AutoRangeMax=true
AutoSpacing=true
kNumMinorDivisions=5
ShowAxisTitle=true
ShowAxisUnits=true
vwm='FullWnd' viewWndWd=#nan
ActivateMargins=true
MarginPercent=0
$end
'LineAxisRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=8
$begin
'LineAxisRenderAttribute' DecimalFieldWidth=3
DecimalFieldPrecision=2
ManualTitle='' AxisColor(R=0, G=0, B=0)
MinScale=0
MaxScale=1
TickSpacing=1
ManualUnits=false
Units='mm' AxisScale='Linear' NumberFormat='Auto' $begin 'TextFont' $begin
'FontAttribute' $begin
'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'TextFont' InfMapMode=false
InfMapValue=1.79769313486232e+306
AutoRangeMin=true
AutoRangeMax=true
AutoSpacing=true
kNumMinorDivisions=5
ShowAxisTitle=true
ShowAxisUnits=true
vwm='FullWnd' viewWndWd=#nan
ActivateMargins=true
MarginPercent=0
$end
'LineAxisRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=9
$begin
'LineAxisRenderAttribute' DecimalFieldWidth=3
DecimalFieldPrecision=2
ManualTitle='' AxisColor(R=0, G=0, B=0)
MinScale=0
MaxScale=1
TickSpacing=1
ManualUnits=false
Units='mm' AxisScale='Linear' NumberFormat='Auto' $begin 'TextFont' $begin
'FontAttribute' $begin
'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'TextFont' InfMapMode=false
InfMapValue=1.79769313486232e+306
AutoRangeMin=true
AutoRangeMax=true
AutoSpacing=true
kNumMinorDivisions=5
ShowAxisTitle=true
ShowAxisUnits=true
vwm='FullWnd' viewWndWd=#nan
ActivateMargins=true
MarginPercent=0
$end
'LineAxisRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=10
$begin
'LineAxisRenderAttribute' DecimalFieldWidth=3
DecimalFieldPrecision=2
ManualTitle='' AxisColor(R=0, G=0, B=0)
MinScale=0
MaxScale=1
TickSpacing=1
ManualUnits=false
Units='mm' AxisScale='Linear' NumberFormat='Auto' $begin 'TextFont' $begin
'FontAttribute' $begin
'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'TextFont' InfMapMode=false
InfMapValue=1.79769313486232e+306
AutoRangeMin=true
AutoRangeMax=true
AutoSpacing=true
kNumMinorDivisions=5
ShowAxisTitle=true
ShowAxisUnits=true
vwm='FullWnd' viewWndWd=#nan
ActivateMargins=true
MarginPercent=0
$end
'LineAxisRenderAttribute' $end 'SubMapItem'
$end 'MainMapItem' $end 'PlotAttributeStoreMap' $end 'DocAttributes' $begin 'DocDefaultAttributes' $begin 'PlotAttributeStoreMap' $end 'PlotAttributeStoreMap' $end 'DocDefaultAttributes' $begin 'PerViewPlotAttributeStoreMap' $begin 'MapItem' ItemID=20
$begin 'PlotAttributeStoreMap' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=4
$begin
'BasicLayoutAttribute' $begin
'LayoutRect' Top=742
Left=584
Bottom=9780
Right=9221
$end
'LayoutRect' $end
'BasicLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=12
$begin
'BasicLayoutAttribute' $begin
'LayoutRect' Top=742
Left=584
Bottom=9780
Right=9221
$end
'LayoutRect' $end
'BasicLayoutAttribute'
$end 'SubMapItem' $begin 'SubMapItem' DataSourceID=19
$begin
'BasicLayoutAttribute' $begin
'LayoutRect' Top=75Left=75Bottom=9925
Right=444
$end
'LayoutRect' $end
'BasicLayoutAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=15
$begin
'CartesianAxisLayoutAttribute' $begin
'AxisRect' Top=75Left=9221
Bottom=9925
Right=9925
$end
'AxisRect' $begin
'GridRect' Top=742
Left=584
Bottom=9780
Right=9221
$end
'GridRect' $end
'CartesianAxisLayoutAttribute'
$end 'SubMapItem' $begin 'SubMapItem' DataSourceID=16
$begin
'CartesianAxisLayoutAttribute' $begin
'AxisRect' Top=75Left=469
Bottom=741
Right=9221
$end
'AxisRect' $begin
'GridRect' Top=742
Left=584
Bottom=9780
Right=9221
$end
'GridRect' $end
'CartesianAxisLayoutAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=4
$begin
'CartesianCurveGroupLayoutAttribute' X_spc=2000000000
X_fwd=4
X_fpr=2
Y1_spc=2.5
Y1_fwd=4
Y1_fpr=2
$end
'CartesianCurveGroupLayoutAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem'
$begin 'SubMapItem' DataSourceID=6
$begin
'DockableOverlayLayoutAttribute' $begin
'Dock_0' $begin
'OverlayLayoutAttribute' $begin 'BoundingRect' Top=4850
Left=544
Bottom=9850
Right=8044
$end 'BoundingRect' ModifySize=false
ModifyPosition=false
$end
'OverlayLayoutAttribute' $end 'Dock_0' $end
'DockableOverlayLayoutAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=26
$begin
'OverlayLayoutAttribute' $begin
'BoundingRect' Top=75Left=75Bottom=4075
Right=4075
$end
'BoundingRect' ModifySize=false
ModifyPosition=false
$end
'OverlayLayoutAttribute' $end 'SubMapItem' $end 'MainMapItem' $end 'PlotAttributeStoreMap' PlotType=1
$end 'MapItem' $end 'PerViewPlotAttributeStoreMap' IsViewAttribServer=false
ViewID=-1
$begin 'SourceIDMap' IDMapItem(4, 0, -1, 21)
$end 'SourceIDMap' $begin 'TraceCharacteristicsMgr' $end 'TraceCharacteristicsMgr' $begin 'CartesianXMarkerManager' RefMarkerID=-1
CurrentMarkerID=-1
$begin 'ReferenceCurves' $end 'ReferenceCurves' $end 'CartesianXMarkerManager' $begin 'CartesianYMarkerManager' $end 'CartesianYMarkerManager' XAxisStackID=-1
$begin 'AllTransSrcDwg' $begin 'PT' ID=1
TransSrcDwg(-1, 0, 19, 1, 15, 2, 16, 5, 6, 11, 12, 21, 22, 23, 24, 25, 26)
$end 'PT' $end 'AllTransSrcDwg' $begin 'AllPtSVID' PtID(1, -1, 4)
$end 'AllPtSVID' $end 'PlotDisplayDataManager' $end 'Report2D' $end 'Return Loss' $begin 'VSWR' ReportID=7
$begin 'Report2D' name='VSWR' ReportID=7
ReportType=0
DisplayType=1
Title='' Domain='' $begin 'Graph2DsV2'
$begin 'Graph2D' TraceDefID=6
Type='Continuous' Axis='Y1' $end 'Graph2D' $end 'Graph2DsV2' $begin 'PlotDisplayDataManager' NextUniqueID=33
MoveBackwards=false
$begin 'PlotHeaderDataSource' CompanyName='' ShowDesignName=true
ProjectFileName='' $end 'PlotHeaderDataSource' StockNameIDMap(AxisX=1, AxisY1=2, AxisY2=8, AxisY3=9, AxisY4=10, Grid=11, Header=0, Legend=5, MarkerLegend=25, XYHorizScroller=7)
$begin 'SourceList' $begin 'ListItem' $begin 'MarkerDataSource' MarkerID=31
MarkerName='m1' AttachedToDrawing=true
CurveID=21
CurveDefinition='Cartesian' PrimarySweepValue='9.7GHz' $end 'MarkerDataSource' $end 'ListItem' $end 'SourceList' $begin 'DocAttributes' $begin 'PlotAttributeStoreMap' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=11
$begin
'CartesianGridDescAttribute' ShowXMinor=true
ShowYMinor=true
ShowXMajor=true
ShowYMajor=true
ShowBorder=true
$end
'CartesianGridDescAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=21
$begin
'CurveCartesianAttribute'
YAxis='Y1' $end
'CurveCartesianAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=21
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=255, G=0, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HorizontalLeftTriangle' SymbolColor(R=0, G=25, B=185)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=0
$begin
'HeaderRenderAttribute' $begin 'TitleFont' $begin
'FontAttribute' $begin
'Font' Height=-19
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'TitleFont' $begin 'SubtitleFont' $begin
'FontAttribute' $begin
'Font' Height=-13
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'SubtitleFont' $end
'HeaderRenderAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=5
$begin
'LegendRenderAttribute' $begin
'LegendTableAttrib' $begin
'TableRenderAttribute' $begin
'TableFontAttrib' $begin 'FontAttribute' $begin 'Font' Height=-11
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end 'Font' Color(R=0, G=0, B=0)
$end 'FontAttribute' $end
'TableFontAttrib' $begin
'TableTitleFontAttrib' $begin 'FontAttribute' $begin 'Font' Height=-11
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end 'Font' Color(R=0, G=0, B=0)
$end 'FontAttribute' $end
'TableTitleFontAttrib' TableBorderLineWidth=1
TableBorderLineColor=0
TableGridLineWidth=1
TableGridLineColor=12632256
TableBackgroundColor=16777215
TableHeaderBackgroundColor=14408667
$end
'TableRenderAttribute' $end
'LegendTableAttrib' ShowTraceName=true
ShowSolutionName=true
ShowVariationKey=true
DockMode='None' $end
'LegendRenderAttribute' $end 'SubMapItem' $end 'MainMapItem'
$begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=1
$begin
'LineAxisRenderAttribute' DecimalFieldWidth=3
DecimalFieldPrecision=2
ManualTitle='' AxisColor(R=0, G=0, B=0)
MinScale=0
MaxScale=1
TickSpacing=1
ManualUnits=false
Units='mm' AxisScale='Linear' NumberFormat='Auto' $begin 'TextFont' $begin
'FontAttribute' $begin
'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'TextFont' InfMapMode=false
InfMapValue=1.79769313486232e+306
AutoRangeMin=true
AutoRangeMax=true
AutoSpacing=true
kNumMinorDivisions=5
ShowAxisTitle=true
ShowAxisUnits=true
vwm='FullWnd' viewWndWd=#nan
ActivateMargins=true
MarginPercent=0
$end
'LineAxisRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=2
$begin
'LineAxisRenderAttribute' DecimalFieldWidth=3
DecimalFieldPrecision=2
ManualTitle='' AxisColor(R=0, G=0, B=0)
MinScale=0
MaxScale=1
TickSpacing=1
ManualUnits=false
Units='mm' AxisScale='Linear' NumberFormat='Auto' $begin 'TextFont'
$begin
'FontAttribute' $begin
'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'TextFont' InfMapMode=false
InfMapValue=1.79769313486232e+306
AutoRangeMin=true
AutoRangeMax=true
AutoSpacing=true
kNumMinorDivisions=5
ShowAxisTitle=true
ShowAxisUnits=true
vwm='FullWnd' viewWndWd=#nan
ActivateMargins=true
MarginPercent=0
$end
'LineAxisRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=8
$begin
'LineAxisRenderAttribute' DecimalFieldWidth=3
DecimalFieldPrecision=2
ManualTitle='' AxisColor(R=0, G=0, B=0)
MinScale=0
MaxScale=1
TickSpacing=1
ManualUnits=false
Units='mm' AxisScale='Linear' NumberFormat='Auto' $begin 'TextFont' $begin
'FontAttribute' $begin
'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'TextFont' InfMapMode=false
InfMapValue=1.79769313486232e+306
AutoRangeMin=true
AutoRangeMax=true
AutoSpacing=true
kNumMinorDivisions=5
ShowAxisTitle=true
ShowAxisUnits=true
vwm='FullWnd' viewWndWd=#nan
ActivateMargins=true
MarginPercent=0
$end
'LineAxisRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=9
$begin
'LineAxisRenderAttribute' DecimalFieldWidth=3
DecimalFieldPrecision=2
ManualTitle='' AxisColor(R=0, G=0, B=0)
MinScale=0
MaxScale=1
TickSpacing=1
ManualUnits=false
Units='mm' AxisScale='Linear' NumberFormat='Auto' $begin 'TextFont' $begin
'FontAttribute' $begin
'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'TextFont' InfMapMode=false
InfMapValue=1.79769313486232e+306
AutoRangeMin=true
AutoRangeMax=true
AutoSpacing=true
kNumMinorDivisions=5
ShowAxisTitle=true
ShowAxisUnits=true
vwm='FullWnd' viewWndWd=#nan
ActivateMargins=true
MarginPercent=0
$end
'LineAxisRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=10
$begin
'LineAxisRenderAttribute' DecimalFieldWidth=3
DecimalFieldPrecision=2
ManualTitle='' AxisColor(R=0, G=0, B=0)
MinScale=0
MaxScale=1
TickSpacing=1
ManualUnits=false
Units='mm' AxisScale='Linear' NumberFormat='Auto' $begin 'TextFont' $begin
'FontAttribute' $begin
'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'TextFont' InfMapMode=false
InfMapValue=1.79769313486232e+306
AutoRangeMin=true
AutoRangeMax=true
AutoSpacing=true
kNumMinorDivisions=5
ShowAxisTitle=true
ShowAxisUnits=true
vwm='FullWnd' viewWndWd=#nan
ActivateMargins=true
MarginPercent=0
$end
'LineAxisRenderAttribute' $end 'SubMapItem' $end 'MainMapItem' $end 'PlotAttributeStoreMap' $end 'DocAttributes' $begin 'DocDefaultAttributes'
$begin 'PlotAttributeStoreMap' $end 'PlotAttributeStoreMap' $end 'DocDefaultAttributes' $begin 'PerViewPlotAttributeStoreMap' $begin 'MapItem' ItemID=20
$begin 'PlotAttributeStoreMap' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=4
$begin
'BasicLayoutAttribute' $begin
'LayoutRect' Top=706
Left=584
Bottom=9780
Right=9221
$end
'LayoutRect' $end
'BasicLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=12
$begin
'BasicLayoutAttribute' $begin
'LayoutRect' Top=706
Left=584
Bottom=9780
Right=9221
$end
'LayoutRect' $end
'BasicLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=19
$begin
'BasicLayoutAttribute' $begin
'LayoutRect' Top=75Left=75Bottom=9925
Right=444
$end
'LayoutRect' $end
'BasicLayoutAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=15
$begin
'CartesianAxisLayoutAttribute' $begin
'AxisRect' Top=75Left=9221
Bottom=9925
Right=9925
$end
'AxisRect' $begin
'GridRect' Top=706
Left=584
Bottom=9780
Right=9221
$end
'GridRect' $end
'CartesianAxisLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=16
$begin
'CartesianAxisLayoutAttribute' $begin
'AxisRect' Top=75Left=469
Bottom=705
Right=9221
$end
'AxisRect' $begin
'GridRect' Top=706
Left=584
Bottom=9780
Right=9221
$end
'GridRect' $end
'CartesianAxisLayoutAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=4
$begin
'CartesianCurveGroupLayoutAttribute' X_spc=2000000000
X_fwd=4
X_fpr=2
Y1_spc=5
Y1_fwd=4
Y1_fpr=2
$end
'CartesianCurveGroupLayoutAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=6
$begin
'DockableOverlayLayoutAttribute' $begin
'Dock_0' $begin
'OverlayLayoutAttribute' $begin 'BoundingRect' Top=4850
Left=544
Bottom=9850
Right=8044
$end 'BoundingRect' ModifySize=false
ModifyPosition=false
$end
'OverlayLayoutAttribute' $end 'Dock_0' $end
'DockableOverlayLayoutAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=26
$begin
'OverlayLayoutAttribute' $begin
'BoundingRect' Top=75Left=75Bottom=4075
Right=4075
$end
'BoundingRect' ModifySize=false
ModifyPosition=false
$end
'OverlayLayoutAttribute' $end 'SubMapItem' $end 'MainMapItem' $end 'PlotAttributeStoreMap' PlotType=1
$end 'MapItem' $end 'PerViewPlotAttributeStoreMap' IsViewAttribServer=false
ViewID=-1
$begin 'SourceIDMap' IDMapItem(6, 0, -1, 21)
$end 'SourceIDMap' $begin 'TraceCharacteristicsMgr' $end 'TraceCharacteristicsMgr' $begin 'CartesianXMarkerManager' RefMarkerID=-1
CurrentMarkerID=-1
$begin 'ReferenceCurves' $end 'ReferenceCurves' $end 'CartesianXMarkerManager' $begin 'CartesianYMarkerManager' $end 'CartesianYMarkerManager' XAxisStackID=-1
$begin 'AllTransSrcDwg' $begin 'PT' ID=1
TransSrcDwg(-1, 0, 19, 1, 15, 2, 16, 5, 6, 11, 12, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32)
$end 'PT' $end 'AllTransSrcDwg' $begin 'AllPtSVID' PtID(1, -1, 4)
$end 'AllPtSVID' $end 'PlotDisplayDataManager' $end 'Report2D' $end 'VSWR' $begin '3D Polar Plot 1' ReportID=9
$begin 'Report3D' name='3D Polar Plot 1' ReportID=9
hasWindowBeenOpened=false
ReportType=3
DisplayType=7
$begin 'Graph3DsV2' $begin 'Graph3DV2' TraceDefID=8
GraphName='dB(GainTotal)'
$begin 'Graph3DV2TraceSettings' IsoValType='Tone' TraceType='Surface' SmoothShade=true
Filled=true
Transparency=0
AddGrid=false
MapColor=false
CurveLineStyle=4
CurveLineWidth=5
CurveMarkStyle=9
CurveMarkSize=5
GridColor(102, 102, 102)
$begin 'OutlineID' AddOutLine=false
Width=4
Style='Solid'
'Outline color'(191, 191, 191)
$end 'OutlineID' $end 'Graph3DV2TraceSettings' $end 'Graph3DV2' $end 'Graph3DsV2' $begin 'PolarReport3DSettings'
'Real time mode'=true
$begin 'ColorMapSettings' ColorMapType='Spectrum' SpectrumType='Rainbow' UniformColor(127, 255, 255)
RampColor(255, 127, 127)
$end 'ColorMapSettings' $begin 'LabelsSettings' ShowTitle=false
TitleText='' ShowAxes=true
SpecifyTitle=false
SpecifyLabel=false
X_Label='X' Y_Label='Y' Z_Label='Z' $end 'LabelsSettings' $begin 'Scale3DSettings' unit=90
m_nLevels=15
minvalue=-28.7696
maxvalue=-3.4
log=false
IntrinsicMin=-28.769553018146
IntrinsicMax=-3.68589845777015
LimitFieldValuePrecision=false
FieldValuePrecisionDigits=4
ScaleType=1
UserSpecifyValues(15, -28.769552230835, -26.9778633117676, -25.1861724853516, -23.3944835662842, -21.6027946472168, -19.8111038208008, -18.0194149017334, -16.227725982666, -14.43603515625, -12.6443462371826, -10.8526554107666, -9.06096649169922, -7.26927757263184, -5.47758674621582, -3.68589854240417)
$end 'Scale3DSettings' $begin 'zAxes' MajorTicksNum=11
MinorTicksNum=5
DisplayMajor=true
DisplayMinor=false
$end 'zAxes' $end 'PolarReport3DSettings' $end 'Report3D' $end '3D Polar Plot 1' $begin '3D Polar Plot 2' ReportID=11
$begin 'Report3D' name='3D Polar Plot 2' ReportID=11
hasWindowBeenOpened=false
ReportType=3
DisplayType=7
$begin 'Graph3DsV2' $begin 'Graph3DV2' TraceDefID=10
GraphName='dB(rETotal)' $begin 'Graph3DV2TraceSettings' IsoValType='Tone' TraceType='Surface' SmoothShade=true
Filled=true
Transparency=0
AddGrid=false
MapColor=false
CurveLineStyle=4
CurveLineWidth=5
CurveMarkStyle=9
CurveMarkSize=5
GridColor(102, 102, 102)
$begin 'OutlineID' AddOutLine=false
Width=4
Style='Solid'
'Outline color'(191, 191, 191)
$end 'OutlineID' $end 'Graph3DV2TraceSettings' $end 'Graph3DV2'
$end 'Graph3DsV2' $begin 'PolarReport3DSettings'
'Real time mode'=true
$begin 'ColorMapSettings' ColorMapType='Spectrum' SpectrumType='Rainbow' UniformColor(127, 255, 255)
RampColor(255, 127, 127)
$end 'ColorMapSettings' $begin 'LabelsSettings' ShowTitle=false
TitleText='' ShowAxes=true
SpecifyTitle=false
SpecifyLabel=false
X_Label='X' Y_Label='Y' Z_Label='Z' $end 'LabelsSettings' $begin 'Scale3DSettings' unit=90
m_nLevels=15
minvalue=-15.6757811143998
maxvalue=9.40787344597607
log=false
IntrinsicMin=-15.6757811143998
IntrinsicMax=9.40787344597607
LimitFieldValuePrecision=false
FieldValuePrecisionDigits=4
ScaleType=0
UserSpecifyValues(15, -15.67578125, -
13.8840913772583, -12.0924015045166, -10.3007125854492, -8.50902271270752, -6.71733283996582, -4.92564392089844, -3.13395404815674, -1.34226417541504, 0.449424743652344, 2.24111557006836, 4.03280448913574, 5.82449340820313, 7.61618423461914, 9.40787315368652)
$end 'Scale3DSettings' $begin 'zAxes' MajorTicksNum=11
MinorTicksNum=5
DisplayMajor=true
DisplayMinor=false
$end 'zAxes' $end 'PolarReport3DSettings' $end 'Report3D' $end '3D Polar Plot 2' $begin 'XY Plot 1' ReportID=13
$begin 'Report2D' name='XY Plot 1' ReportID=13
ReportType=3
DisplayType=1
Title='' Domain='' $begin 'Graph2DsV2' $begin 'Graph2D' TraceDefID=12
Type='Continuous' Axis='Y1' $end 'Graph2D' $end 'Graph2DsV2' $begin 'PlotDisplayDataManager' NextUniqueID=95
MoveBackwards=false
$begin 'PlotHeaderDataSource' CompanyName='' ShowDesignName=true
ProjectFileName='' $end 'PlotHeaderDataSource' StockNameIDMap(AxisX=1, AxisY1=2, AxisY2=8, AxisY3=9, AxisY4=10, Grid=11, Header=0, Legend=5, XYHorizScroller=7)
$begin 'SourceList' $end 'SourceList' $begin 'DocAttributes' $begin 'PlotAttributeStoreMap' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=11
$begin
'CartesianGridDescAttribute' ShowXMinor=true
ShowYMinor=true
ShowXMajor=true
ShowYMajor=true
ShowBorder=true
$end
'CartesianGridDescAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=21
$begin
'CurveCartesianAttribute' YAxis='Y1' $end
'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem'
DataSourceID=23 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=25 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=27 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=29 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=31 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=33 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=35
$begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=37 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=39 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=41 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=43 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=45 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=47
$begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=49 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=51 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=53 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=55 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=57 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=59
$begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=61 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=63 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=65 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=67 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=69 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=71
$begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=73 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=75 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=77 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=79 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=81 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=83
$begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=85 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=87 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=89 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=91 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=93 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem'
DataSourceID=21
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=255, G=0, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HorizontalLeftTriangle' SymbolColor(R=0, G=25, B=185)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=23
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=128, G=64, B=100)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowCircle' SymbolColor(R=128, G=0, B=128)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=25
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=0, G=0, B=200)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='VerticalDownTriangle' SymbolColor(R=192, G=192, B=192)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=27
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=80, G=0, B=80)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowVerticalEllipse' SymbolColor(R=111, G=111, B=111)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=29
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=128, G=128, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='VerticalEllipse' SymbolColor(R=240, G=130, B=19)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=31
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=200, G=0, B=128)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowVerticalDownTriangle'
SymbolColor(R=128, G=0, B=0)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=33
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=15, G=160, B=180)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='Circle' SymbolColor(R=0, G=128, B=128)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=35
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=0, G=128, B=128)
$end
'LineRenderAttribute' TraceType='Continuous'
SymbolType='HollowHorizontalLeftTriangle' SymbolColor(R=15, G=160, B=180)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=37
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=128, G=0, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HorizontalLeftTriangle' SymbolColor(R=200, G=0, B=128)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=39
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=240, G=130, B=19)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowCircle' SymbolColor(R=128, G=128, B=0)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=41
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=111, G=111, B=111)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='VerticalDownTriangle' SymbolColor(R=80, G=0, B=80)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=43
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid'
LineWidth=1LineColor(R=192, G=192, B=192)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowVerticalEllipse' SymbolColor(R=0, G=0, B=200)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=45
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=128, G=0, B=128)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='VerticalEllipse' SymbolColor(R=128, G=64, B=100)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=47
$begin
'CurveRenderAttribute'
$begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=255, G=0, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowVerticalDownTriangle' SymbolColor(R=0, G=25, B=185)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=49
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=255, G=0, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HorizontalLeftTriangle' SymbolColor(R=0, G=25, B=185)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem'
DataSourceID=51
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=128, G=64, B=100)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowCircle' SymbolColor(R=128, G=0, B=128)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=53
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=0, G=0, B=200)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='VerticalDownTriangle' SymbolColor(R=192, G=192, B=192)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=55
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=80, G=0, B=80)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowVerticalEllipse' SymbolColor(R=111, G=111, B=111)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=57
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=128, G=128, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='VerticalEllipse' SymbolColor(R=240, G=130, B=19)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=59
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=200, G=0, B=128)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowVerticalDownTriangle' SymbolColor(R=128, G=0, B=0)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=61
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=15, G=160, B=180)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='Circle'
SymbolColor(R=0, G=128, B=128)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=63
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=0, G=128, B=128)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowHorizontalLeftTriangle' SymbolColor(R=15, G=160, B=180)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=65
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=128, G=0, B=0)
$end
'LineRenderAttribute'
TraceType='Continuous' SymbolType='HorizontalLeftTriangle' SymbolColor(R=200, G=0, B=128)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=67
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=240, G=130, B=19)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowCircle' SymbolColor(R=128, G=128, B=0)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=69
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1
LineColor(R=111, G=111, B=111)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='VerticalDownTriangle' SymbolColor(R=80, G=0, B=80)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=71
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=192, G=192, B=192)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowVerticalEllipse' SymbolColor(R=0, G=0, B=200)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=73
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute'
LineStyle='Solid' LineWidth=1LineColor(R=128, G=0, B=128)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='VerticalEllipse' SymbolColor(R=128, G=64, B=100)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=75
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=255, G=0, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowVerticalDownTriangle' SymbolColor(R=0, G=25, B=185)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=77
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=255, G=0, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HorizontalLeftTriangle' SymbolColor(R=0, G=25, B=185)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=79
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=128, G=64, B=100)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowCircle' SymbolColor(R=128, G=0, B=128)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute'
$end 'SubMapItem' $begin 'SubMapItem' DataSourceID=81
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=0, G=0, B=200)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='VerticalDownTriangle' SymbolColor(R=192, G=192, B=192)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=83
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=80, G=0, B=80)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowVerticalEllipse' SymbolColor(R=111, G=111, B=111)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=85
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=128, G=128, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='VerticalEllipse' SymbolColor(R=240, G=130, B=19)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=87
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=200, G=0, B=128)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowVerticalDownTriangle' SymbolColor(R=128, G=0, B=0)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=89
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=15, G=160, B=180)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='Circle' SymbolColor(R=0, G=128, B=128)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=91
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=0, G=128, B=128)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowHorizontalLeftTriangle'
SymbolColor(R=15, G=160, B=180)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=93
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=128, G=0, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HorizontalLeftTriangle' SymbolColor(R=200, G=0, B=128)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=0
$begin
'HeaderRenderAttribute' $begin 'TitleFont' $begin
'FontAttribute' $begin
'Font' Height=-19
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'TitleFont' $begin 'SubtitleFont' $begin
'FontAttribute' $begin
'Font' Height=-13
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'SubtitleFont' $end
'HeaderRenderAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=5
$begin
'LegendRenderAttribute' $begin
'LegendTableAttrib' $begin
'TableRenderAttribute' $begin
'TableFontAttrib' $begin 'FontAttribute' $begin 'Font' Height=-11
Width=0
Escapement=0 Orientation=0 Weight=400 Italic=0 Underline=0 StrikeOut=0 CharSet=0 OutPrecision=7 ClipPrecision=48 Quality=6 PitchAndFamily=0 FaceName='Arial' $end 'Font' Color(R=0, G=0, B=0) $end 'FontAttribute' $end 'TableFontAttrib' $begin 'TableTitleFontAttrib' $begin 'FontAttribute' $begin 'Font' Height=-11 Width=0 Escapement=0 Orientation=0 Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end 'Font' Color(R=0, G=0, B=0)
$end 'FontAttribute' $end
'TableTitleFontAttrib' TableBorderLineWidth=1
TableBorderLineColor=0
TableGridLineWidth=1
TableGridLineColor=12632256
TableBackgroundColor=16777215
TableHeaderBackgroundColor=14408667
$end
'TableRenderAttribute' $end
'LegendTableAttrib' ShowTraceName=true
ShowSolutionName=true
ShowVariationKey=true
DockMode='None'
$end
'LegendRenderAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=1
$begin
'LineAxisRenderAttribute' DecimalFieldWidth=3
DecimalFieldPrecision=2
ManualTitle='' AxisColor(R=0, G=0, B=0)
MinScale=0
MaxScale=1
TickSpacing=1
ManualUnits=false
Units='mm' AxisScale='Linear' NumberFormat='Auto' $begin 'TextFont' $begin
'FontAttribute' $begin
'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'TextFont' InfMapMode=false
InfMapValue=1.79769313486232e+306
AutoRangeMin=true
AutoRangeMax=true
AutoSpacing=true
kNumMinorDivisions=5
ShowAxisTitle=true
ShowAxisUnits=true
vwm='FullWnd' viewWndWd=#nan
ActivateMargins=true
MarginPercent=0
$end
'LineAxisRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=2
$begin
'LineAxisRenderAttribute' DecimalFieldWidth=3
DecimalFieldPrecision=2
ManualTitle='' AxisColor(R=0, G=0, B=0)
MinScale=0
MaxScale=1
TickSpacing=1
ManualUnits=false
Units='mm'
AxisScale='Linear' NumberFormat='Auto' $begin 'TextFont' $begin
'FontAttribute' $begin
'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'TextFont' InfMapMode=false
InfMapValue=1.79769313486232e+306
AutoRangeMin=true
AutoRangeMax=true
AutoSpacing=true
kNumMinorDivisions=5
ShowAxisTitle=true
ShowAxisUnits=true
vwm='FullWnd' viewWndWd=#nan
ActivateMargins=true
MarginPercent=0
$end
'LineAxisRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=8
$begin
'LineAxisRenderAttribute' DecimalFieldWidth=3
DecimalFieldPrecision=2
ManualTitle='' AxisColor(R=0, G=0, B=0)
MinScale=0
MaxScale=1
TickSpacing=1
ManualUnits=false
Units='mm' AxisScale='Linear' NumberFormat='Auto' $begin 'TextFont' $begin
'FontAttribute' $begin
'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'TextFont' InfMapMode=false
InfMapValue=1.79769313486232e+306
AutoRangeMin=true
AutoRangeMax=true
AutoSpacing=true
kNumMinorDivisions=5
ShowAxisTitle=true
ShowAxisUnits=true
vwm='FullWnd' viewWndWd=#nan
ActivateMargins=true
MarginPercent=0
$end
'LineAxisRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=9
$begin
'LineAxisRenderAttribute' DecimalFieldWidth=3
DecimalFieldPrecision=2
ManualTitle='' AxisColor(R=0, G=0, B=0)
MinScale=0
MaxScale=1
TickSpacing=1
ManualUnits=false
Units='mm' AxisScale='Linear' NumberFormat='Auto' $begin 'TextFont' $begin
'FontAttribute' $begin
'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'TextFont' InfMapMode=false
InfMapValue=1.79769313486232e+306
AutoRangeMin=true
AutoRangeMax=true
AutoSpacing=true
kNumMinorDivisions=5
ShowAxisTitle=true
ShowAxisUnits=true
vwm='FullWnd' viewWndWd=#nan
ActivateMargins=true
MarginPercent=0
$end
'LineAxisRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=10
$begin
'LineAxisRenderAttribute' DecimalFieldWidth=3
DecimalFieldPrecision=2
ManualTitle='' AxisColor(R=0, G=0, B=0)
MinScale=0
MaxScale=1
TickSpacing=1
ManualUnits=false
Units='mm' AxisScale='Linear' NumberFormat='Auto' $begin 'TextFont' $begin
'FontAttribute' $begin
'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'TextFont' InfMapMode=false
InfMapValue=1.79769313486232e+306
AutoRangeMin=true
AutoRangeMax=true
AutoSpacing=true
kNumMinorDivisions=5
ShowAxisTitle=true
ShowAxisUnits=true
vwm='FullWnd' viewWndWd=#nan
ActivateMargins=true
MarginPercent=0
$end
'LineAxisRenderAttribute' $end 'SubMapItem'
$end 'MainMapItem' $end 'PlotAttributeStoreMap' $end 'DocAttributes' $begin 'DocDefaultAttributes' $begin 'PlotAttributeStoreMap' $end 'PlotAttributeStoreMap' $end 'DocDefaultAttributes' $begin 'PerViewPlotAttributeStoreMap' $begin 'MapItem' ItemID=20
$begin 'PlotAttributeStoreMap' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=4
$begin
'BasicLayoutAttribute' $begin
'LayoutRect' Top=806
Left=895
Bottom=9695
Right=8904
$end
'LayoutRect' $end
'BasicLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=12
$begin
'BasicLayoutAttribute' $begin
'LayoutRect' Top=806
Left=895
Bottom=9695
Right=8904
$end
'LayoutRect' $end
'BasicLayoutAttribute'
$end 'SubMapItem' $begin 'SubMapItem' DataSourceID=19
$begin
'BasicLayoutAttribute' $begin
'LayoutRect' Top=75Left=75Bottom=9925
Right=681
$end
'LayoutRect' $end
'BasicLayoutAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=15
$begin
'CartesianAxisLayoutAttribute' $begin
'AxisRect' Top=75Left=8904
Bottom=9925
Right=9925
$end
'AxisRect' $begin
'GridRect' Top=806
Left=895
Bottom=9695
Right=8904
$end
'GridRect' $end
'CartesianAxisLayoutAttribute'
$end 'SubMapItem' $begin 'SubMapItem' DataSourceID=16
$begin
'CartesianAxisLayoutAttribute' $begin
'AxisRect' Top=75Left=706
Bottom=805
Right=8904
$end
'AxisRect' $begin
'GridRect' Top=806
Left=895
Bottom=9695
Right=8904
$end
'GridRect' $end
'CartesianAxisLayoutAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=4
$begin
'CartesianCurveGroupLayoutAttribute' X_spc=0.872664625997165
X_fwd=5
X_fpr=2
Y1_spc=5
Y1_fwd=4
Y1_fpr=2
$end
'CartesianCurveGroupLayoutAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem'
$begin 'SubMapItem' DataSourceID=6
$begin
'DockableOverlayLayoutAttribute' $begin
'Dock_0' $begin
'OverlayLayoutAttribute' $begin 'BoundingRect' Top=4850
Left=781
Bottom=9850
Right=8281
$end 'BoundingRect' ModifySize=false
ModifyPosition=false
$end
'OverlayLayoutAttribute' $end 'Dock_0' $end
'DockableOverlayLayoutAttribute' $end 'SubMapItem' $end 'MainMapItem' $end 'PlotAttributeStoreMap' PlotType=1
$end 'MapItem' $end 'PerViewPlotAttributeStoreMap' IsViewAttribServer=false
ViewID=-1
$begin 'SourceIDMap' IDMapItem(12, 0, -1, 21)
IDMapItem(12, 1, -1, 23)
IDMapItem(12, 2, -1, 25)
IDMapItem(12, 3, -1, 27)
IDMapItem(12, 4, -1, 29)
IDMapItem(12, 5, -1, 31)
IDMapItem(12, 6, -1, 33)
IDMapItem(12, 7, -1, 35)
IDMapItem(12, 8, -1, 37)
IDMapItem(12, 9, -1, 39)
IDMapItem(12, 10, -1, 41)
IDMapItem(12, 11, -1, 43)
IDMapItem(12, 12, -1, 45)
IDMapItem(12, 13, -1, 47)
IDMapItem(12, 14, -1, 49)
IDMapItem(12, 15, -1, 51)
IDMapItem(12, 16, -1, 53)
IDMapItem(12, 17, -1, 55)
IDMapItem(12, 18, -1, 57)
IDMapItem(12, 19, -1, 59)
IDMapItem(12, 20, -1, 61)
IDMapItem(12, 21, -1, 63)
IDMapItem(12, 22, -1, 65)
IDMapItem(12, 23, -1, 67)
IDMapItem(12, 24, -1, 69)
IDMapItem(12, 25, -1, 71)
IDMapItem(12, 26, -1, 73)
IDMapItem(12, 27, -1, 75)
IDMapItem(12, 28, -1, 77)
IDMapItem(12, 29, -1, 79)
IDMapItem(12, 30, -1, 81)
IDMapItem(12, 31, -1, 83)
IDMapItem(12, 32, -1, 85)
IDMapItem(12, 33, -1, 87)
IDMapItem(12, 34, -1, 89)
IDMapItem(12, 35, -1, 91)
IDMapItem(12, 36, -1, 93)
$end 'SourceIDMap' $begin 'TraceCharacteristicsMgr' $end 'TraceCharacteristicsMgr' $begin 'CartesianXMarkerManager' RefMarkerID=-1
CurrentMarkerID=-1
$begin 'ReferenceCurves' $end 'ReferenceCurves' $end 'CartesianXMarkerManager' $begin 'CartesianYMarkerManager' $end 'CartesianYMarkerManager' XAxisStackID=-1
$begin 'AllTransSrcDwg' $begin 'PT' ID=1
TransSrcDwg(-1, 0, 19, 1, 15, 2, 16, 5, 6, 11, 12, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94)
$end 'PT' $end 'AllTransSrcDwg' $begin 'AllPtSVID' PtID(1, -1, 4)
$end 'AllPtSVID' $end 'PlotDisplayDataManager' $end 'Report2D' $end 'XY Plot 1' $begin 'Radiation Pattern 1' ReportID=15
$begin 'Report2D' name='Radiation Pattern 1' ReportID=15
ReportType=3
DisplayType=3
Title='' Domain='' $begin 'Graph2DsV2' $begin 'Graph2D' TraceDefID=14
Type='Continuous' Axis='Y1' $end 'Graph2D' $end 'Graph2DsV2' $begin 'PlotDisplayDataManager' NextUniqueID=84
MoveBackwards=false
$begin 'PlotHeaderDataSource' CompanyName='' ShowDesignName=true
ProjectFileName='' $end 'PlotHeaderDataSource' StockNameIDMap(CircleAxis=4, Header=0, Legend=2, PolarGrid=6)
$begin 'SourceList' $end 'SourceList' $begin 'DocAttributes' $begin 'PlotAttributeStoreMap' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=10
$begin
'CurveCartesianAttribute' YAxis='Y1' $end
'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=12
$begin
'CurveCartesianAttribute' YAxis='Y1'
$end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=14 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=16 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=18 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=20 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=22 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=24 $begin 'CurveCartesianAttribute' YAxis='Y1'
$end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=26 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=28 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=30 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=32 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=34 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=36 $begin 'CurveCartesianAttribute' YAxis='Y1'
$end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=38 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=40 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=42 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=44 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=46 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=48 $begin 'CurveCartesianAttribute' YAxis='Y1'
$end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=50 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=52 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=54 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=56 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=58 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=60 $begin 'CurveCartesianAttribute' YAxis='Y1'
$end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=62 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=64 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=66 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=68 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=70 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=72 $begin 'CurveCartesianAttribute' YAxis='Y1'
$end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=74 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=76 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=78 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=80 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=82 $begin 'CurveCartesianAttribute' YAxis='Y1' $end 'CurveCartesianAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=10 $begin 'CurveRenderAttribute'
$begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=255, G=0, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HorizontalLeftTriangle' SymbolColor(R=0, G=25, B=185)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=12
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=128, G=64, B=100)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowCircle' SymbolColor(R=128, G=0, B=128)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem'
DataSourceID=14
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=0, G=0, B=200)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='VerticalDownTriangle' SymbolColor(R=192, G=192, B=192)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=16
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=80, G=0, B=80)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowVerticalEllipse' SymbolColor(R=111, G=111, B=111)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=18
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=128, G=128, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='VerticalEllipse' SymbolColor(R=240, G=130, B=19)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=20
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=200, G=0, B=128)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowVerticalDownTriangle' SymbolColor(R=128, G=0, B=0)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=22
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=15, G=160, B=180)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='Circle' SymbolColor(R=0, G=128, B=128)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=24
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=0, G=128, B=128)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowHorizontalLeftTriangle'
SymbolColor(R=15, G=160, B=180)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=26
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=128, G=0, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HorizontalLeftTriangle' SymbolColor(R=200, G=0, B=128)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=28
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=240, G=130, B=19)
$end
'LineRenderAttribute'
TraceType='Continuous' SymbolType='HollowCircle' SymbolColor(R=128, G=128, B=0)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=30
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=111, G=111, B=111)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='VerticalDownTriangle' SymbolColor(R=80, G=0, B=80)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=32
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1
LineColor(R=192, G=192, B=192)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowVerticalEllipse' SymbolColor(R=0, G=0, B=200)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=34
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=128, G=0, B=128)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='VerticalEllipse' SymbolColor(R=128, G=64, B=100)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=36
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute'
LineStyle='Solid' LineWidth=1LineColor(R=255, G=0, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowVerticalDownTriangle' SymbolColor(R=0, G=25, B=185)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=38
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=255, G=0, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HorizontalLeftTriangle' SymbolColor(R=0, G=25, B=185)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=40
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=128, G=64, B=100)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowCircle' SymbolColor(R=128, G=0, B=128)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=42
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=0, G=0, B=200)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='VerticalDownTriangle' SymbolColor(R=192, G=192, B=192)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute'
$end 'SubMapItem' $begin 'SubMapItem' DataSourceID=44
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=80, G=0, B=80)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowVerticalEllipse' SymbolColor(R=111, G=111, B=111)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=46
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=128, G=128, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='VerticalEllipse' SymbolColor(R=240, G=130, B=19)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=48
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=200, G=0, B=128)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowVerticalDownTriangle' SymbolColor(R=128, G=0, B=0)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=50
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=15, G=160, B=180)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='Circle' SymbolColor(R=0, G=128, B=128)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=52
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=0, G=128, B=128)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowHorizontalLeftTriangle' SymbolColor(R=15, G=160, B=180)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=54
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=128, G=0, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HorizontalLeftTriangle'
SymbolColor(R=200, G=0, B=128)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=56
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=240, G=130, B=19)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowCircle' SymbolColor(R=128, G=128, B=0)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=58
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=111, G=111, B=111)
$end
'LineRenderAttribute'
TraceType='Continuous' SymbolType='VerticalDownTriangle' SymbolColor(R=80, G=0, B=80)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=60
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=192, G=192, B=192)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowVerticalEllipse' SymbolColor(R=0, G=0, B=200)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=62
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1
LineColor(R=128, G=0, B=128)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='VerticalEllipse' SymbolColor(R=128, G=64, B=100)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=64
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=255, G=0, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowVerticalDownTriangle' SymbolColor(R=0, G=25, B=185)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=66
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute'
LineStyle='Solid' LineWidth=1LineColor(R=255, G=0, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HorizontalLeftTriangle' SymbolColor(R=0, G=25, B=185)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=68
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=128, G=64, B=100)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowCircle' SymbolColor(R=128, G=0, B=128)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=70
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=0, G=0, B=200)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='VerticalDownTriangle' SymbolColor(R=192, G=192, B=192)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=72
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=80, G=0, B=80)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowVerticalEllipse' SymbolColor(R=111, G=111, B=111)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute'
$end 'SubMapItem' $begin 'SubMapItem' DataSourceID=74
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=128, G=128, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='VerticalEllipse' SymbolColor(R=240, G=130, B=19)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=76
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=200, G=0, B=128)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowVerticalDownTriangle' SymbolColor(R=128, G=0, B=0)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=78
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=15, G=160, B=180)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='Circle' SymbolColor(R=0, G=128, B=128)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=80
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=0, G=128, B=128)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HollowHorizontalLeftTriangle' SymbolColor(R=15, G=160, B=180)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=82
$begin
'CurveRenderAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1LineColor(R=128, G=0, B=0)
$end
'LineRenderAttribute' TraceType='Continuous' SymbolType='HorizontalLeftTriangle' SymbolColor(R=200, G=0, B=128)
ShowSymbols=false
SymbolFrequency=15
ShowArrows=false
$end
'CurveRenderAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=0
$begin
'HeaderRenderAttribute' $begin 'TitleFont' $begin
'FontAttribute' $begin
'Font' Height=-19
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'TitleFont' $begin 'SubtitleFont' $begin
'FontAttribute' $begin
'Font' Height=-13
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'SubtitleFont' $end
'HeaderRenderAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=2
$begin
'LegendRenderAttribute' $begin
'LegendTableAttrib' $begin
'TableRenderAttribute' $begin
'TableFontAttrib' $begin 'FontAttribute' $begin 'Font' Height=-11
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end 'Font' Color(R=0, G=0, B=0)
$end 'FontAttribute' $end
'TableFontAttrib' $begin
'TableTitleFontAttrib' $begin 'FontAttribute' $begin 'Font' Height=-11
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end 'Font' Color(R=0, G=0, B=0)
$end 'FontAttribute' $end
'TableTitleFontAttrib' TableBorderLineWidth=1
TableBorderLineColor=0
TableGridLineWidth=1
TableGridLineColor=12632256
TableBackgroundColor=16777215
TableHeaderBackgroundColor=14408667
$end
'TableRenderAttribute' $end
'LegendTableAttrib' ShowTraceName=true
ShowSolutionName=true
ShowVariationKey=true
DockMode='None' $end
'LegendRenderAttribute' $end 'SubMapItem' $end 'MainMapItem'
$begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=4
$begin
'PolarCircleAxisAttribute' CircDecimalFieldWidth=3
CircDecimalFieldPrecision=2
CircleAxisMinorDivCount=6
CircleAxisMajorDivCount=12
$begin
'FontAttribute' $begin 'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end 'Font' Color(R=0, G=0, B=0)
$end 'FontAttribute' $begin
'LineRenderAttribute'
LineStyle='Solid' LineWidth=1LineColor(R=0, G=0, B=0)
$end
'LineRenderAttribute' $end
'PolarCircleAxisAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=6
$begin
'PolarGridAttribute' ShowGridLabels=true
$begin 'CircleGrid' $begin
'FontAttribute' $begin
'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1
LineColor(R=200, G=200, B=200)
$end
'LineRenderAttribute' $end 'CircleGrid' $begin 'AngleGrid' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1
LineColor(R=220, G=220, B=220)
$end
'LineRenderAttribute' $end 'AngleGrid' $begin
'ImpedanceGrid' $begin
'ImpedanceRGrid' $begin
'FontAttribute' $begin 'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end 'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1
LineColor(R=200, G=200, B=200)
$end
'LineRenderAttribute' $end
'ImpedanceRGrid' $begin
'ImpedanceXGrid' $begin
'FontAttribute' $begin 'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end 'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1
LineColor(R=220, G=220, B=220)
$end
'LineRenderAttribute' $end
'ImpedanceXGrid' $end
'ImpedanceGrid' $begin
'AdimittanceGrid' $begin
'AdimittanceGGrid' $begin
'FontAttribute'
$begin 'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end 'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1
LineColor(R=200, G=200, B=200)
$end
'LineRenderAttribute' $end
'AdimittanceGGrid'
$begin
'AdimittanceBGrid' $begin
'FontAttribute' $begin 'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end 'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $begin
'LineRenderAttribute' LineStyle='Solid' LineWidth=1
LineColor(R=220, G=220, B=220)
$end
'LineRenderAttribute' $end
'AdimittanceBGrid' $end
'AdimittanceGrid' $end 'PolarGridAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=-1
$begin
'PolarPlotRenderAttribute' ShowCircleGrid=true
ShowAngleGrid=true
ShowImpedanceGrid=true
ShowAdmittanceGrid=false
$end
'PolarPlotRenderAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=6
$begin
'PolarRhoAxisAttribute' DecimalFieldWidth=3
DecimalFieldPrecision=2
ManualTitle='' AxisColor(R=0, G=0, B=0)
MinScale=-20
MaxScale=10
TickSpacing=6
ManualUnits=false
Units='' AxisScale='Linear' NumberFormat='Auto' $begin 'TextFont' $begin
'FontAttribute'
$begin
'Font' Height=-12
Width=0
Escapement=0
Orientation=0
Weight=400
Italic=0
Underline=0
StrikeOut=0
CharSet=0
OutPrecision=7
ClipPrecision=48
Quality=6
PitchAndFamily=0
FaceName='Arial' $end
'Font' Color(R=0, G=0, B=0)
$end
'FontAttribute' $end 'TextFont' InfMapMode=false
InfMapValue=1.79769313486232e+306
AutoRangeMin=true
AutoRangeMax=true
AutoSpacing=true
kNumMinorDivisions=5
ShowAxisTitle=true
ShowAxisUnits=true
vwm='FullWnd' viewWndWd=#nan
ActivateMargins=true
MarginPercent=0
$end
'PolarRhoAxisAttribute' $end 'SubMapItem' $end 'MainMapItem' $end 'PlotAttributeStoreMap' $end 'DocAttributes' $begin 'DocDefaultAttributes' $begin 'PlotAttributeStoreMap' $end 'PlotAttributeStoreMap' $end 'DocDefaultAttributes' $begin 'PerViewPlotAttributeStoreMap' $begin 'MapItem' ItemID=9
$begin 'PlotAttributeStoreMap' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=1
$begin
'BasicLayoutAttribute' $begin
'LayoutRect' Top=780
Left=9023
Bottom=9220
Right=583
$end
'LayoutRect' $end
'BasicLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=8
$begin
'BasicLayoutAttribute' $begin
'LayoutRect' Top=75Left=75Bottom=9925
Right=444
$end
'LayoutRect' $end
'BasicLayoutAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=3
$begin
'DockableOverlayLayoutAttribute' $begin
'Dock_0' $begin
'OverlayLayoutAttribute' $begin 'BoundingRect' Top=4850
Left=544
Bottom=9850
Right=8044
$end 'BoundingRect' ModifySize=false
ModifyPosition=false
$end
'OverlayLayoutAttribute' $end 'Dock_0' $end
'DockableOverlayLayoutAttribute' $end 'SubMapItem' $end 'MainMapItem' $begin 'MainMapItem' $begin 'SubMapItem' DataSourceID=5
$begin
'PolarLayoutAttribute' $begin
'PolarCircleRect' Top=780
Left=9023
Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=7 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect'
Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=11 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect'
$begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=13 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0
$end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=15 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=17 $begin 'PolarLayoutAttribute'
$begin
'PolarCircleRect' Top=780
Left=9023
Bottom=9220
Right=583
$end
'PolarCircleRect' $begin
'AxisRect' Top=244687312
Left=0
Bottom=0
Right=0
$end
'AxisRect' $begin
'AxisLabelRect' Top=0
Left=0
Bottom=359399424
Right=0
$end
'AxisLabelRect' $end
'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=19
$begin
'PolarLayoutAttribute' $begin
'PolarCircleRect' Top=780
Left=9023
Bottom=9220
Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=21 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0
Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=23 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0
Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=25 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute'
$end 'SubMapItem' $begin 'SubMapItem' DataSourceID=27 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=29 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780
Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=31 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect'
$begin
'AxisRect' Top=244687312
Left=0
Bottom=0
Right=0
$end
'AxisRect' $begin
'AxisLabelRect' Top=0
Left=0
Bottom=359399424
Right=0
$end
'AxisLabelRect' $end
'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=33
$begin
'PolarLayoutAttribute' $begin
'PolarCircleRect' Top=780
Left=9023
Bottom=9220
Right=583
$end
'PolarCircleRect' $begin
'AxisRect' Top=244687312
Left=0
Bottom=0
Right=0
$end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=35 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424
Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=37 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=39
$begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=41 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023
Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=43 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect'
Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=45 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect'
$begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=47 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0
$end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=49 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=51 $begin 'PolarLayoutAttribute'
$begin
'PolarCircleRect' Top=780
Left=9023
Bottom=9220
Right=583
$end
'PolarCircleRect' $begin
'AxisRect' Top=244687312
Left=0
Bottom=0
Right=0
$end
'AxisRect' $begin
'AxisLabelRect' Top=0
Left=0
Bottom=359399424
Right=0
$end
'AxisLabelRect' $end
'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=53
$begin
'PolarLayoutAttribute' $begin
'PolarCircleRect' Top=780
Left=9023
Bottom=9220
Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=55 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0
Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=57 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0
Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=59 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute'
$end 'SubMapItem' $begin 'SubMapItem' DataSourceID=61 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=63 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780
Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=65 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect'
$begin
'AxisRect' Top=244687312
Left=0
Bottom=0
Right=0
$end
'AxisRect' $begin
'AxisLabelRect' Top=0
Left=0
Bottom=359399424
Right=0
$end
'AxisLabelRect' $end
'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=67
$begin
'PolarLayoutAttribute' $begin
'PolarCircleRect' Top=780
Left=9023
Bottom=9220
Right=583
$end
'PolarCircleRect' $begin
'AxisRect' Top=244687312
Left=0
Bottom=0
Right=0
$end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=69 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424
Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=71 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=73
$begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=75 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023
Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=77 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect'
Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=79 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect'
$begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0 $end 'AxisLabelRect' $end 'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=81 $begin 'PolarLayoutAttribute' $begin 'PolarCircleRect' Top=780 Left=9023 Bottom=9220 Right=583 $end 'PolarCircleRect' $begin 'AxisRect' Top=244687312 Left=0 Bottom=0 Right=0 $end 'AxisRect' $begin 'AxisLabelRect' Top=0 Left=0 Bottom=359399424 Right=0
$end
'AxisLabelRect' $end
'PolarLayoutAttribute' $end 'SubMapItem' $begin 'SubMapItem' DataSourceID=83
$begin
'PolarLayoutAttribute' $begin
'PolarCircleRect' Top=780
Left=9023
Bottom=9220
Right=583
$end
'PolarCircleRect' $begin
'AxisRect' Top=244687312
Left=0
Bottom=0
Right=0
$end
'AxisRect' $begin
'AxisLabelRect' Top=0
Left=0
Bottom=359399424
Right=0
$end
'AxisLabelRect' $end
'PolarLayoutAttribute' $end 'SubMapItem' $end 'MainMapItem' $end 'PlotAttributeStoreMap' PlotType=3
$end 'MapItem'
$end 'PerViewPlotAttributeStoreMap' IsViewAttribServer=false
ViewID=-1
$begin 'SourceIDMap' IDMapItem(14, 0, -1, 10)
IDMapItem(14, 1, -1, 12)
IDMapItem(14, 2, -1, 14)
IDMapItem(14, 3, -1, 16)
IDMapItem(14, 4, -1, 18)
IDMapItem(14, 5, -1, 20)
IDMapItem(14, 6, -1, 22)
IDMapItem(14, 7, -1, 24)
IDMapItem(14, 8, -1, 26)
IDMapItem(14, 9, -1, 28)
IDMapItem(14, 10, -1, 30)
IDMapItem(14, 11, -1, 32)
IDMapItem(14, 12, -1, 34)
IDMapItem(14, 13, -1, 36)
IDMapItem(14, 14, -1, 38)
IDMapItem(14, 15, -1, 40)
IDMapItem(14, 16, -1, 42)
IDMapItem(14, 17, -1, 44)
IDMapItem(14, 18, -1, 46)
IDMapItem(14, 19, -1, 48)
IDMapItem(14, 20, -1, 50)
IDMapItem(14, 21, -1, 52)
IDMapItem(14, 22, -1, 54)
IDMapItem(14, 23, -1, 56)
IDMapItem(14, 24, -1, 58)
IDMapItem(14, 25, -1, 60)
IDMapItem(14, 26, -1, 62)
IDMapItem(14, 27, -1, 64)
IDMapItem(14, 28, -1, 66)
IDMapItem(14, 29, -1, 68)
IDMapItem(14, 30, -1, 70)
IDMapItem(14, 31, -1, 72)
IDMapItem(14, 32, -1, 74)
IDMapItem(14, 33, -1, 76)
IDMapItem(14, 34, -1, 78)
IDMapItem(14, 35, -1, 80)
IDMapItem(14, 36, -1, 82)
$end 'SourceIDMap' $begin 'TraceCharacteristicsMgr' $end 'TraceCharacteristicsMgr' $begin 'CartesianXMarkerManager' RefMarkerID=-1
CurrentMarkerID=-1
$begin 'ReferenceCurves' $end 'ReferenceCurves'
$end 'CartesianXMarkerManager' $begin 'CartesianYMarkerManager' $end 'CartesianYMarkerManager' XAxisStackID=-1
$begin 'AllTransSrcDwg' $begin 'PT' ID=3
TransSrcDwg(-1, 0, 8, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83)
$end 'PT' $end 'AllTransSrcDwg' $begin 'AllPtSVID' PtID(3, -1, 1)
$end 'AllPtSVID' $end 'PlotDisplayDataManager' $end 'Report2D' $end 'Radiation Pattern 1' $begin '3D Polar Plot 3' ReportID=17
$begin 'Report3D' name='3D Polar Plot 3' ReportID=17
hasWindowBeenOpened=false
ReportType=3
DisplayType=7
$begin 'Graph3DsV2' $begin 'Graph3DV2' TraceDefID=16
GraphName='dB(DirTotal)' $begin 'Graph3DV2TraceSettings' IsoValType='Tone' TraceType='Surface' SmoothShade=true
Filled=true
Transparency=0
AddGrid=false
MapColor=false
CurveLineStyle=4
CurveLineWidth=5
CurveMarkStyle=9
CurveMarkSize=5
GridColor(102, 102, 102)
$begin 'OutlineID' AddOutLine=false
Width=4
Style='Solid'
'Outline color'(191, 191, 191)
$end 'OutlineID' $end 'Graph3DV2TraceSettings' $end 'Graph3DV2' $end 'Graph3DsV2' $begin 'PolarReport3DSettings'
'Real time mode'=true
$begin 'ColorMapSettings' ColorMapType='Spectrum' SpectrumType='Rainbow' UniformColor(127, 255, 255)
RampColor(255, 127, 127)
$end 'ColorMapSettings' $begin 'LabelsSettings' ShowTitle=false
TitleText='' ShowAxes=true
SpecifyTitle=false
SpecifyLabel=false
X_Label='X' Y_Label='Y' Z_Label='Z' $end 'LabelsSettings' $begin 'Scale3DSettings' unit=90
m_nLevels=15
minvalue=-28.5391
maxvalue=13.45543
log=false
IntrinsicMin=-28.5390874635618
IntrinsicMax=-3.45543290318587
LimitFieldValuePrecision=false
FieldValuePrecisionDigits=4
ScaleType=1
UserSpecifyValues(15, -28.5390872955322, -26.7473983764648, -24.9557075500488, -23.1640186309814, -21.3723297119141, -19.580638885498, -17.7889499664307, -15.997260093689, -14.2055702209473, -12.4138813018799, -10.6221904754639, -8.83050155639648, -7.0388126373291, -5.24712181091309, -3.4554328918457)
$end 'Scale3DSettings' $begin 'zAxes' MajorTicksNum=11
MinorTicksNum=5
DisplayMajor=true
DisplayMinor=false
$end 'zAxes' $end 'PolarReport3DSettings' $end 'Report3D' $end '3D Polar Plot 3' $end 'Reports' $begin 'ReportsWindowInfoList'
$begin 'Return Loss' ReportID=5
$begin 'WindowInfoList' $begin 'Report2D' $begin 'ViewInfo' $begin 'WrapperView' ID(20)
$end 'WrapperView' $begin 'WrapperDoc' HiddenDrawings()
$begin 'DispType' PlotType=1
$begin 'CurveMed' $begin 'MedCamera' $begin 'svrc' svid=4
view(20, cam(XYCam(false, true, true, true, 0, 1, 0, 1, 0, 1, 0, 1, 6.8663624751916e-044, 46.5570220947266)))
$end 'svrc' $end 'MedCamera' $end 'CurveMed' $end 'DispType' $end 'WrapperDoc' WindowPos(WindowPos(5, 160, 409, -8, -31, 26, 26, 1002, 333))
$end 'ViewInfo' $end 'Report2D' $end 'WindowInfoList' $end 'Return Loss' $begin 'VSWR' ReportID=7
$begin 'WindowInfoList' $begin 'Report2D' $begin 'ViewInfo' $begin 'WrapperView' ID(20)
$end 'WrapperView' $begin 'WrapperDoc' HiddenDrawings()
$begin 'DispType' PlotType=1
$begin 'CurveMed' $begin 'MedCamera' $begin 'svrc' svid=4
view(20, cam(XYCam(false, true, true, true, 0, 1, 0, 1, 0, 1, 0, 1, 1.47136338754106e-043, 7.62247510057199e039)))
$end 'svrc'
$end 'MedCamera' $end 'CurveMed' $end 'DispType' $end 'WrapperDoc' WindowPos(WindowPos(5, 0, 409, -8, -31, 52, 52, 1028, 359))
$end 'ViewInfo' $end 'Report2D' $end 'WindowInfoList' $end 'VSWR' $begin '3D Polar Plot 1' ReportID=9
$begin 'WindowInfoList' R3DWindowPos(Editor3d(View(WindowPos(5, -1, -1, -8, -31, 78, 78, 1054, 385), OrientationMatrix(-0.155902400612831, -0.25, 0.395284742116928, 0, 0.467707216739655, -0.0833333358168602, 0.131761580705643, 0, 0, 0.416666686534882, 0.263523191213608, 0, 0, 2.38418579101563e-007, -5.74868392944336, 1, 0, -1.49223613739014, 1.52977609634399, -0.363942325115204, 0.470588266849518, 0.625207901000977, 10.8721599578857), Drawings[1: 'dB(GainTotal)'])))
$end 'WindowInfoList' $end '3D Polar Plot 1' $begin '3D Polar Plot 2' ReportID=11
$begin 'WindowInfoList' R3DWindowPos(Editor3d(View(WindowPos(5, -1, -1, -8, -31, 104, 104, 1080, 411), OrientationMatrix(-0.155902400612831, -0.25, 0.395284742116928, 0, 0.467707216739655, -0.0833333358168602, 0.131761580705643, 0, 0, 0.416666686534882, 0.263523191213608, 0, 0, 2.38418579101563e-007, -5.74868392944336, 1, 0, -3.62121200561523, 3.62121200561523, -1, 1, 0.625207901000977, 10.8721599578857), Drawings[1: 'dB(rETotal)'])))
$end 'WindowInfoList' $end '3D Polar Plot 2' $begin 'XY Plot 1' ReportID=13
$begin 'WindowInfoList' $begin 'Report2D' $begin 'ViewInfo' $begin 'WrapperView' ID(20)
$end 'WrapperView' $begin 'WrapperDoc' HiddenDrawings()
$begin 'DispType' PlotType=1
$begin 'CurveMed' $begin 'MedCamera' $begin 'svrc' svid=4
view(20, cam(XYCam(false, true, true, true, 0, 1, 0, 1, 0, 1, 0, 1, 6.58610278232664e-044, 6.8663624751916e-044)))
$end 'svrc' $end 'MedCamera' $end 'CurveMed' $end 'DispType' $end 'WrapperDoc' WindowPos(WindowPos(5, -1, -1, -8, -31, 130, 130, 1106, 437))
$end 'ViewInfo' $end 'Report2D' $end 'WindowInfoList' $end 'XY Plot 1' $begin 'Radiation Pattern 1' ReportID=15
$begin 'WindowInfoList' $begin 'Report2D' $begin 'ViewInfo' $begin 'WrapperView' ID(9)
$end 'WrapperView' $begin 'WrapperDoc' HiddenDrawings()
$begin 'DispType' PlotType=3
$begin 'CurveMed' $begin 'MedCamera' $begin 'svrc' svid=1
view(9, cam(PolCam(-1, 1, -1, 1, 930, 266)))
$end 'svrc' $end 'MedCamera' $end 'CurveMed' $end 'DispType' $end 'WrapperDoc' WindowPos(WindowPos(3, -1, -1, -8, -31, 0, 0, 976, 307))
$end 'ViewInfo' $end 'Report2D' $end 'WindowInfoList' $end 'Radiation Pattern 1' $begin '3D Polar Plot 3' ReportID=17
$begin 'WindowInfoList' R3DWindowPos(Editor3d(View(WindowPos(5, -1, -1, -8, -31, 26, 26, 1002, 333), OrientationMatrix(-0.155902400612831, -0.25, 0.395284742116928, 0, 0.467707216739655, -0.0833333358168602, 0.131761580705643, 0, 0, 0.416666686534882, 0.263523191213608, 0, 0, 2.38418579101563e-007, -5.74868392944336, 1, 0, -3.62121200561523, 3.62121200561523, -1, 1, 0.625207901000977, 10.8721599578857), Drawings[1: 'dB(DirTotal)'])))
$end 'WindowInfoList'
$end '3D Polar Plot 3' $end 'ReportsWindowInfoList' $end 'ReportSetup' $begin 'Properties' $end 'Properties' $begin 'UserDefinedDocument' $begin 'Data' $end 'Data' $end 'UserDefinedDocument' $end 'HfssDesignInstance' $end 'Instance' $end 'DataInstances' $begin 'WBSystemIDToDesignInstanceIDMap' $end 'WBSystemIDToDesignInstanceIDMap' $begin 'WBSysIDSysDetails' $end 'WBSysIDSysDetails' $begin 'WBConnIDConnDetails' $end 'WBConnIDConnDetails' $end 'AnsoftProject' $begin 'ProjectPreview' Thumbnail64='/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQE\
BAQICAQECAQEBAgICAgICAgICAQICAgICAgICAgL/2wBDAQEBAQEBAQEBAQECAQEBAgICAgICAgI
CAg\
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgL/wAARCABgAGADASIAAhEBAxEB/\
8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQR\
BRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUp\
TVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5us\
LDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAA\
AECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHB\
CSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ\
3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4u\
Pk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD+/iiiigAooooAKKKKACiiigAooooAKKKKACiiv\
N/i/wDFHw98Fvhn4z+KPie21bU9L8H6NNqEPh7w5DY3vi7xnrk8kWn+Fvh/4E0nUNQtY/EXxE8ReJ7z\
SND8O6SLiKbVtb8QWGmW7G4u4lNRjKcowiryk0ku7eiR0YPCYnH4vC4HB0XiMZjakKNKnH4p1KklCEI\
+cpSUV5sdqXxh+Eei/Erw/wDBnWPin8OdJ+MHi3SJ/EHhX4Ual438M2HxK8TaBbRa5Pca54f8C3Wppq\
mtaRHB4Z8SO9zbWssKJ4fvmZwLScx+jV+LnwZ+Amj63+0h+1do/wC0Z4W+HfxW8b/HP9m79hr4k/tJ6\
XqehWXi34UeKfinZeN/2sdCjsfDHhTxVoqQD4eeHtN+HfgfR/C8d5YDUzpvgPS9U1241LxTNq2t6h9K\
Q/sU/sz6Nu/4V38OJ/gN9px/bH/DLfjn4jfsn/8ACV+Tn+z/APhOv+GavF3hT/hPvsPm339mf219v/s\
r+2NQ/s77L/aV/wDae6rhsNSkoOvNtRg21CMotyjGTcW5xaim2ldNtJSdublj+nZ/wbwZkuOp5bPibH\
1K9HCYCrUq0Mvw2Kw9eri8DhsZVqYec8xwNSGHhUxEqFBVKdSpWpUYYuo6E8S8FhP0Por4Di+DXxu8
P\
+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' $begin 'DesignInfo' DesignName='HFSSDesign1' Notes='' Factory='HFSS' IsSolved=true
'Nominal Setups'[1: 'Setup1']
'Optimetrics Setups'[0:]
'Optimetrics Experiment Types'[0:]
Image64='/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQE\
BAQICAQECAQEBAgICAgICAgICAQICAgICAgICAgL/2wBDAQEBAQEBAQEBAQECAQEBAgICAgICAgI
CAg\
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgL/wAARCADIAMgDASIAAhEBAxEB/\
8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQR\
BRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUp\
TVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5us\
LDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAA\
AECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHB\
CSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ\
3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4u\
Pk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD+/iiiigAooooAKKKKACiiigAooooAKKKKACiii\
gAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACii\
igAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACi\
iigAooooAKKKKACiiigAoorkPiD488KfCzwF43+J3jzVf7C8D/Djwh4l8eeM9c+w6lqn9jeFPCGjXvi\
HxFqv9m6NZ3F5qP2fSNOvJvItLee5m8ny4IZZWVGaTk1GKcpSdklq23sku5th8PXxdehhcLQnicTiZx\
p06dOMp1KlSclGEIQinKc5yajGMU5Sk0km2fO/7UvjHXtQHg39m3wJrWreGPG37Q+k/Ea21vx14c1K/\
0Txd8I/gh4Q0Cx0/4ofFzwJqlvNbInxEtvEvjz4V+GfDrJe/a9H1v4s2HjH+yPEOj+FNb0i5+FP2K/2\
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
v/AfwJ\
8IfA3V2/dXPiz9mKXXP2VfHuo6a3zzeHdX+IX7N2r+Fdc1nwhNdJZ3Nxo13qE2k3F7pGn309nJeadYz\
2+bN+xzNo6ix+Fv7VH7Wfwm8OyMLu88PRePvAPx7a91pgYbjWj42/bG+FvxL8U6asljFp8H9lWOv2nh\
+H+zRd2ujwajeape3/2bRXR9bxP2q0qi7TfPH/wGfMvnbQ+ujx7xi3bFcRYnNqPWjj5/2jh2+knhses\
Rh3OO8Juk5wd3Fps+Ipvh7+3DoTDWk+JP7JnxXFmoH/CuIvgv8Zf2dF8RGcm23H4zT/H/AOKx8GtaCc\
XvHgTXRqH9ljSsaWb46zp+XN8Qf2nfCwex8afsZeLfGOszN9ssr79mn42/A34ieAYNLlbyIbDWvEX7R\
viv4Oa5a+MEnt72S4tbTwpfaStncafNBrtxd3F/p+lfeNFUsU3rUoU6j72cNO1qcoR+bV/OyVt48aSq\
+/mfDOVZtXWiqPD18DaC1UPY5Rictw0rScpe1nQliJc3LKtKnClCn+fs37W3wk0HanxOs/iv8DPsObb\
xfrvxy+B3xf8Ahj8Kfh/rMWLa40XxZ+0j4i8FJ8LznWyul2Gp6b411HQNe1K5tLbw3q+s/wBp6W9782\
/teftVfs1eIP2ZvEvxK8HfHb4VfETwR8EP2g/2HfG3xZ174WeN9A+KsXgTwxp/7Z3wT1uXVNds/hze6\
pcwLLpfhnxBLaRJC899/Y9wllFcSRsg/ZSvOfGnwe+EfxJ1/wADeKviJ8LPhz4+8UfDDV28QfDTxJ40\
8EeGfFOv/DzX2vdI1Jtc8DaxrmmT3HhLVzqPh/QJzc6fJbzGbRLOXfvtoWTahicLTrUqsqM17OUZO04\
u/K07JOCte1k3J8t+a0rcr97hzi3grKs/yPOMVw5mdOOVYzDYuao5nhqimsNXhXlQp06mWU5U1XVN4e\
FapiK0sIqixE6eNdF4ev5T+zT8NfFPhuy8ffFL4oaUuk/F342+LZvEWu6NNfaZrN18PPhv4d8/QPgr8\
HodU065vY7NdH8ERrq3iDTbDWNZ8PRfEf4keP8AV/Dd/NpWuRO/05RRXFUqSqzlOVk5dFsklZJeSSSX\
kj8+zfNMRnWY4nMsVGFOpiHFRp001So0qcI0qNCkpSnKNGhRhTo0oynOSpwipSk05MoooqDzQooooAK\
KKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA\
KKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAoooo\
AKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooA//2Q==' $end 'DesignInfo' $end 'ProjectPreview'
