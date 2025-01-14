###################################################
#  This module stitches images and store it as slices
###################################################

import imagej
import os
from config.definitions import ROOT_DIR
import shutil
# initialize ImageJ2 with Fiji plugins
''' 
the fiji version plugins only supports the stitching tool we required from the imagej library.
'''
ij = imagej.init('sc.fiji:fiji')
# print(f"ImageJ2 version: {ij.getVersion()}")

''' 
stitch class

we would be using stitch class for the development of different stitching profiles/ functions  required based on the
data set we have for example random order  we have specific profile which for that data . similarly we can use 
profiles in case of specific orderly stitching like left to right , top to bottom etc
'''


class Stitch:
    def __init__(self):
        # by default DataLocation and OutputDirectory variables point to test data provided with the module.
        self.DataLocation = os.path.join(ROOT_DIR, '50')
        self.OutputDirectory = os.path.join(ROOT_DIR, 'output')
        self.grid_size_x = "1"
        self.grid_size_y = "1"
        self.tile_overlap = "0"
        self.first_file_index_i = "42"
        self.file_names = "{ii}.jpg"

        ''' 
        Random order profile
        in this profile we would be stitching images which does not have any specific order related to them , 
        nor have any overlap specified to them . The fusion method we use is linear blending.
        '''

    def RandomOrder(self, DataLocation, OutputDirectory):
        self.DataLocation = DataLocation
        self.OutputDirectory = OutputDirectory
        plugin = 'Grid/Collection stitching'
        args = {

            'type': '[Unknown position]',
            'order': '[All files in directory]',
            'directory': self.DataLocation,
            'confirm_files'
            'output_textfile_name': 'TileConfiguration.txt',
            'fusion_method': '[Linear Blending]',
            'regression_threshold': '0.30',
            'max/avg_displacement_threshold': '2.50',
            'absolute_displacement_threshold': '3.50',
            'computation_parameters': '[Save memory (but be slower)]',
            'image_output': '[Write to disk]',
            'OutputDirectory': self.OutputDirectory
        }
        ij.py.run_plugin(plugin, args)
        #print("stitching complete in random order the results can be viewed at " + self.OutputDirectory)
        for i in range(1, 4):
            shutil.move(os.path.join(ROOT_DIR, self.DataLocation + '/img_t1_z1_c' + str(i)), os.path.join(ROOT_DIR, 'output'))

        return
        """
        SnakeRowsRightDown
        
        This function takes in grid type data with its two dimensions. You have to specify the file start/end index ,
        The file name format , along with input and output formats. The resulting format is in  tiff. This can be viewed by 
        imagej tool. In the future capabilities to get data from multiple folders and also need to have the ability to get data from multiple 
        folders
        
        """



    def SnakeRowsRightDown(self,DataLocation, OutputDirectory,grid_size_x,grid_size_y,tile_overlap,first_file_index_i,file_names):
        self.DataLocation = DataLocation
        self.OutputDirectory = OutputDirectory
        self.grid_size_x = grid_size_x
        self.grid_size_y = grid_size_y
        self.tile_overlap = tile_overlap
        self.first_file_index_i = first_file_index_i
        self.file_names = file_names

        plugin = 'Grid/Collection stitching'
        args = {

            'type': '[Grid: snake by rows]',
            'order': '[Right & Down]',
            'grid_size_x': str(self.grid_size_x),
            'grid_size_y': str(self.grid_size_y),
            'tile_overlap': str(self.tile_overlap),
            'first_file_index_i': str(self.first_file_index_i),
            'directory': self.DataLocation,
            'file_names': str(self.file_names),
            'confirm_files'
            'output_textfile_name': 'TileConfiguration.txt',
            'fusion_method': '[Linear Blending]',
            'regression_threshold': '0.30',
            'max/avg_displacement_threshold': '2.50',
            'absolute_displacement_threshold': '3.50',
            'computation_parameters': '[Save memory (but be slower)]',
            'image_output': '[Write to disk]',
            'output_directory': self.OutputDirectory
        }
        ij.py.run_plugin(plugin, args)
        return

        """
            testing function
            this function tests all the profiles in the  given class. This removes all the test datafiles . Then it 
            runs the stitch command and see if  producing proper files.
        """


    def Test(self):
        # here FileNumber variable helps in iterate through file name and remove  files before each test
        for FileNumber in range(1, 4):
            pass
            #os.remove("output/img_t1_z1_c" + str(FileNumber))
        self.RandomOrder(self.DataLocation,self.OutputDirectory)

        # here we will be using FileNumber variable to go through files
        Counter = 0
        for FileNumber in range(1, 4):
            print("50/img_t1_z1_c" + str(FileNumber)+"")
            if os.path.exists("50/img_t1_z1_c" + str(FileNumber)+""):
                Counter += 1
            else:
                print("  image slice " + str(FileNumber) + " is not formed after stitching.")
        print(Counter)
        if Counter == 3:
            print("stitching using random method  successful")
        else:
            print(" stitching has issues for the function random_order")
        return
