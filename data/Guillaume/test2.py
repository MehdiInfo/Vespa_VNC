import vtk

# Load a mesh file
reader = vtk.vtkPolyDataReader()
reader.SetFileName("am_t02.vtk")
reader.Update()

mesh = reader.GetOutput()

# Create an ID filter to assign unique IDs to each vertex
id_filter = vtk.vtkIdFilter()
id_filter.SetInputData(mesh)
id_filter.SetPointIdsArrayName("VertexIDs")
id_filter.Update()

# Create a threshold filter to select a single vertex
threshold_filter = vtk.vtkThresholdPoints()
threshold_filter.SetInputConnection(id_filter.GetOutputPort())
threshold_filter.SetInputArrayToProcess(0, 0, 0, vtk.vtkDataObject.FIELD_ASSOCIATION_POINTS, "VertexIDs")
threshold_filter.ThresholdBetween(10, 10)  # select vertex with ID=10

# Create a transform filter to move the selected vertex
transform_filter = vtk.vtkTransformFilter()
transform = vtk.vtkTransform()
transform.Translate(0.1, 0.2, 0.3)  # move the vertex by (0.1, 0.2, 0.3)
transform_filter.SetTransform(transform)
transform_filter.SetInputConnection(threshold_filter.GetOutputPort())
transform_filter.Update()

# Update the mesh with the transformed vertex
mesh.DeepCopy(transform_filter.GetOutput())

# Create a mapper and an actor for the transformed mesh
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(mesh)

actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Create a renderer and a render window
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)

render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)

# Create an interactor and set the render window
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Start the interaction
interactor.Initialize()
interactor.Start()