import os

import h5py
import numpy as np
import open3d
from plyfile import PlyData, PlyElement

class IO:
    @classmethod
    def get(cls, file_path):
        _, file_extension = os.path.splitext(file_path)

        if file_extension in ['.npy']:
            return cls._read_npy(file_path)
        elif file_extension in ['.pcd', '.ply']:
            return cls._read_pcd(file_path)
        elif file_extension in ['.h5']:
            return cls._read_h5(file_path)
        elif file_extension in ['.txt', '.xyz', '.pts']:
            return cls._read_txt(file_path)
        else:
            raise Exception('Unsupported file extension: %s' % file_extension)

    # References: https://github.com/numpy/numpy/blob/master/numpy/lib/format.py
    @classmethod
    def _read_npy(cls, file_path):
        return np.load(file_path)
       
    # References: https://github.com/dimatura/pypcd/blob/master/pypcd/pypcd.py#L275
    # Support PCD files without compression ONLY!
    @classmethod
    def _read_pcd(cls, file_path):
        pc = open3d.io.read_point_cloud(file_path)
        ptcloud = np.array(pc.points)
        return ptcloud

    @classmethod
    def _read_txt(cls, file_path):
        return np.loadtxt(file_path)

    @classmethod
    def _read_h5(cls, file_path):
        f = h5py.File(file_path, 'r')
        return f['data'][()]

def write_ply(points, colors, filename, text=True):
    """ input: Nx3 array of points, Nx3 array of RGB colors (0-255), write points to filename as PLY format. """
    
    # Convert points and colors to tuples
    data = []
    for i in range(points.shape[0]):
        x, y, z = points[i]
        r, g, b = colors[i]
        data.append((x, y, z, r, g, b))

    # Create structured array
    vertex = np.array(data, dtype=[('x', 'f4'), ('y', 'f4'), ('z', 'f4'), ('red', 'f4'), ('green', 'f4'), ('blue', 'f4')])

    # Create PlyElement and PlyData objects
    vertex_element = PlyElement.describe(vertex, 'vertex', comments=['vertices'])
    ply_data = PlyData([vertex_element], text=text)

    # Write to file
    ply_data.write(filename)

def define_color(points):
    colors = np.empty_like(points)
    for i in range(points.shape[0]):
        if i < points.shape[0] // 4:
            colors[i] = [255,0,0] # red
        elif points.shape[0] // 4 <= i < points.shape[0] // 2:
            colors[i] = [0,255,0] # green
        elif points.shape[0] // 2 <= i < 3 * points.shape[0] // 4:
            colors[i] = [0,0,255] # blue  
        else:
            colors[i] = [255,255,0] # yellow
    return colors 

if __name__ == "__main__":

    root_path = 'Input PLY'
    output_path = 'Input PLY'

    io = IO()

    for root, dirs, files in os.walk(root_path):
        for filename in files:
            try:
                points = io.get(os.path.join(root, filename))[:,:3]
                colors = define_color(points)
                write_ply(points, colors, os.path.join(output_path, filename[:-4] + ".ply"))
            except:
                pass
