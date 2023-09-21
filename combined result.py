import nbformat

# List of notebook files to combine
notebook_files = ["notebooks/2-LogisticRegression.ipynb", "notebooks/3-RandomForest.ipynb", "notebooks/4-SVM.ipynb","notebooks/5-XGboost.ipynb"]

# Create an empty combined notebook
combined_nb = nbformat.v4.new_notebook()

# Iterate through the notebook files
for notebook_file in notebook_files:
    with open(notebook_file, "r") as f:
        nb = nbformat.read(f, as_version=4)
        
        # Find the last code cell with output in the notebook
        last_output = None
        for cell in reversed(nb.cells):
            if cell.cell_type == "code" and hasattr(cell, "outputs") and cell.outputs:
                last_output = cell.outputs[-1]  # Get the last output in the cell
                break
        
        # Add the last output with the notebook name at the top (if found)
        if last_output:
            notebook_name = f"Notebook: {notebook_file}"
            combined_nb.cells.append(nbformat.v4.new_markdown_cell(notebook_name))
            combined_nb.cells.append(nbformat.v4.new_code_cell(source=last_output["text"]))

# Save the combined notebook with notebook names and last results to a new file
with open("combined_last_results_with_names.ipynb", "w") as f:
    nbformat.write(combined_nb, f)
