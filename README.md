# This is a WIP and will change a lot

---

- The working file is the .ipynb at the moment as I got tired of creating new files for minor updates.

- I have added requirements files because I was testing on windows11 and wanted to use GPU for training.
  - This lead to issues because tensorflow-2.10.x was the last to natively support GPU on windows. After downgrading everything else broke. Now I don't have to go through dependency hell again trying to find what works together. Just install pip-tools and run along

---

- The notebook allows for prototyping easily (when there isn't as much in there as there is now lol)
  - The notebook has the main gui application that allows for video recording
  - After that there is a section to create a csv of points for model training
  - Then there is a training function
  - Lastly there is a test function
    - The md sections make it easier to find the different application sections

# Getting started

---

If you don't care about running the training on a gpu in Windows 11 you should be able to run the cell blocks in order.
I think the only issues you will run into are these lines:

- `tf.config.experimental.list_physical_devices("GPU")`
  - just remove the `experimental` from the line
  - `tf.config.experimental.list_physical_devices("GPU")` turns into `tf.config.list_physical_devices("GPU")`

---

If you want to run this setup exactly as I have it, here are my suggestions:

- create a conda environment like this `create conda -n env_name_here python=3.10
- once created `pip install pip-tools`
- navigate into the root directory of this project and `pip-sync rexuirements.txt`
- once everything is done ignore the `pip install...` code blocks in the notebook and run the sections of code that you are interested in
