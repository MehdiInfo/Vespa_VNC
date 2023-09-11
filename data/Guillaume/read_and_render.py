import vtk

# Define the file names and colors for each object
file_names = ["am_t02_3D.vtk","am_t02.vtk"]
colors = [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0)]

# Create a renderer and a render window
renderer = vtk.vtkRenderer()
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)

# Create an interactor and set the render window
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)
actors = []
# Loop over the file names and create a pipeline for each file
for i, file_name in enumerate(file_names):
    # Try to read the file as structured
    reader = vtk.vtkDataSetReader()
    reader.SetFileName(file_name)
    reader.Update()
    dataset_type = reader.GetOutput().GetDataObjectType()
    if(dataset_type == vtk.VTK_UNSTRUCTURED_GRID):
        is_structured = False
    else:
        is_structured = True

    # If reading as structured fails, try to read as unstructured
    if not is_structured:
        reader = vtk.vtkUnstructuredGridReader()
        reader.SetFileName(file_name)
        try:
            reader.Update()
            print(f"Reading {file_name} as unstructured data")
        except:
            raise ValueError(f"Unsupported file type for {file_name}")
    else:
        print(f"Reading {file_name} as structured data")

    # Create a mapper and set the input data
    mapper = vtk.vtkPolyDataMapper() if is_structured else vtk.vtkDataSetMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    # Create an actor and set the mapper and color
    actors.append(vtk.vtkActor())
    actors[i].SetMapper(mapper)
    actors[i].GetProperty().SetColor(colors[i])

    # Add the actor to the renderer
    renderer.AddActor(actors[i])

# Set the background color and start the rendering loop
renderer.SetBackground(0.1, 0.2, 0.4)

##
# Define the translation and rotation factors
translation_factor = 0.01
rotation_factor = 0.1
# Define the callback function for mouse events
def mouse_callback(obj, event):
    # Get the interactor and the renderer
    interactor = obj
    renderer = interactor.GetRenderWindow().GetRenderers().GetFirstRenderer()

    # Get the mouse position and the last mouse position
    x, y = interactor.GetEventPosition()
    last_x, last_y = interactor.GetLastEventPosition()

    # Compute the translation and rotation vectors
    translation = [(x - last_x) * translation_factor, (last_y - y) * translation_factor, 0.0]
    rotation = [(y - last_y) * rotation_factor, (x - last_x) * rotation_factor, 0.0]

    # Apply the translation and rotation to the actor
    actor = renderer.GetActors().GetLastItem()
    actor.AddPosition(translation)
    actor.RotateX(rotation[0])
    actor.RotateY(rotation[1])
    actor.RotateZ(rotation[2])
    actor.RotateT(rotation[3])

    # Update the render window
    interactor.Render()
# Add the mouse callback function to the interactor
interactor.AddObserver("MouseMoveEvent", mouse_callback)

interactor.Initialize()
render_window.Render()
interactor.Start()
