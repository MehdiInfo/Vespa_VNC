import vtk

# Create an unstructured grid reader and set the file name
reader = vtk.vtkUnstructuredGridReader()
reader.SetFileName("surface_mesh_closed.vtk")

# Update the reader
reader.Update()

# Create a mapper and set the input data
mapper = vtk.vtkDataSetMapper()
mapper.SetInputData(reader.GetOutput())

# Create an actor and set the mapper
actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Create a renderer and add the actor
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)

renderer = vtk.vtkRenderer(actor2)
renderer = new.renderer(part2)
# Create a render window and add the renderer
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)

# Create an interactor and set the render window
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Initialize the interactor and start the rendering loop
interactor.Initialize()
render_window.Render()
interactor.Start()