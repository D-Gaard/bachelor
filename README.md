# Bachelor Thesis Repository
Contains all code written durring bachelor project regarding "sparse angle reconstruction using segmented coronary angiograms" by Andreas Leerbeck, Mads Daugaard \& Emil Riis-Jacobsen.  

Faculty of Science University of Copenhagen.  

Handed in: June 13. 2022.  

# Versions
Python v.3.9.0  
Jupyter Notebook v.6.1.5  
Visual Studio Code v.1.67.2  
Numpy (v.1.22.3) for quickly handling images in 2D arrays and voxel spaces in 3D arrays.  
OpenCV (v.4.5.5.62) for image processing and thresholding.  
Scipy (v.1.5.4) for n-dimensional transformations.  
PyTorch (v.1.10.2) & Monai (v.0.8.0) for Neural Network   functionality and U-Net training.
Scikit-learn (v.0.23.2) for metric calculations.  
Mayavi (v.4.7.4) for interactive 3D voxel rendering.  
MatPlotLib.pyplot (v) for plotting and visualising 2D images.  
Natsort (v.8.1.0) & Glob (v.3.9.0) for file and path handling.  

# File explanation
Note that all provided carm imaging data has been removed from the github.  
  
File explaniations Weka:  
wekaEvaluation.ipynb - File for calculating weka model metrics.  
weka_vALL.zip - File containing the trained weka model.  

Folders explained  Weka:  
WekaOut - Folder of Weka model predictions on test dataset.  

File explaniations Unet:  
getData.py - File responsible for creating Test/Train/Validation and retriving the files.  
createThresholds4All.ipynb - File for thresholding images.  
createHistograms4All.ipynb - Create histograms for image sequences.  
ALL_4l_rotFlip_1000epochs.pth - Best trained model.  
model_train.ipynb - Unet training file.  
model_metrics.ipynb - Calculate metrics on model with and without post processing.  
predictSegmentations.ipynb - load model and predict on test data.  


Folders explained Unet:  
Prototype - Contains files used to prototype and test functionality.  
Visualisation - Contains files used to create visuals for the report.  
TestSegmentations - Best trained models prediction on test data.  
SegmentationModels - Folder containing all trained Unet models.    
    

File explaniations 3D:  
project3dTo2d.ipynb - File for creating perspective projections of digital 3D model  
reconstructionUncertainty.ipynb - File for visualizing and calculating the metrics for the 9 angle reconstruction.  
reconstructionTranslationRotation.ipynb - File for calculating the translation and rotational metrics.  
solid_400001-segmentation-solid_400001-label.nrrd - Bitmap for 3D digital model.  
projectionTranslation.ipynb - File for creating the translational offset back-projections.  
projectionTotal.ipynb - File for creating the 9 back-projections.  
projectionRotation.ipynb - File for creating the rotational offset back-projections.  
projectionDocAngles.ipynb - File for creating the back-projections with the doctor angles.  
lineRenderWorldSetup.py - File containing all logic for 2D -> 3D back-projections.  
lineRenderAlgo.py - File containing the Bresenham implementation.  
_3dTo2dSetup.py - File for handeling all 3D -> 2D logic.  
  
Folders explained 3D:  
Snapshots - Contains output images from 3D reconstruction.  
Prototype - Contains files used to prototype and test functionality  
Visualisation - Contains files used to create visuals for the report  
Data - The segmentations for the chosen frames  
3dTo2d - Outputs of 2D projected images used  