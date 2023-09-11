import vtk

# Read the VTK file
reader = vtk.vtkPolyDataReader()
reader.SetFileName("surface_mesh_ideal_model.vtk")

reader.Update()

# Get the polydata object
polydata = reader.GetOutput()

tri_converter = vtk.vtkTriangleFilter()
tri_converter.SetInputDataObject(polydata)
tri_converter.Update()
tri_mesh = tri_converter.GetOutput()
#mass_props = vtk.vtkMassProperties()
#mass_props.SetInputDataObject(tri_mesh)
#self._volume_vtk = mass_props.GetVolume()

# Create an implicit modeller
modeller = vtk.vtkImplicitModeller()
modeller.SetInputData(tri_mesh)

# Create a mapper and set the input data
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(tri_converter.GetOutputPort())

# Create an actor and set the mapper
actor = vtk.vtkActor()
actor.SetMapper(mapper)

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)

render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)

# Set up the interactor style
style = vtk.vtkInteractorStyleTrackballCamera()

# Set up the interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)
interactor.SetInteractorStyle(style)
writer = vtk.vtkPolyDataWriter()

writer.SetInputData(tri_mesh)
writer.SetFileName('surface_mesh_ideal_model_triang.vtk')
writer.Update()

# Add the modeller to the interactor
# modeller.SetInteractor(interactor)

#interactor.Start()
