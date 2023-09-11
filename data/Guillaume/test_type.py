import vtk

# Define the file names
file_names = ["am_t02.vtk", "am_t02_3D.vtk"]

# Loop over the file names and create a pipeline for each file
for i, file_name in enumerate(file_names):
    # Read the file
    reader = vtk.vtkDataSetReader()
    reader.SetFileName(file_name)
    reader.Update()

    # Check the dataset type
    dataset_type = reader.GetOutput().GetDataObjectType()
    is_unstructured = dataset_type == vtk.VTK_UNSTRUCTURED_GRID

    print(f"File {i+1}: {file_name}")
    print(f"  Dataset type: {dataset_type}")
    print(f"  Is unstructured: {is_unstructured}")