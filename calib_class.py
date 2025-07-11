import numpy as np
from scipy.optimize import least_squares
from copy import deepcopy

class CameraCalibrationErrorModel:
    '''
    Model different errors in camera calibration.

    Equations implemented from the following references:

    R1: Inferring Bias and Uncertainty in Camera Calibration  
        Annika Hagemann, Moritz Knorr, Holger Janssen, Christoph Stiller  
        International Journal of Computer Vision (2022)  
        https://doi.org/10.1007/s11263-021-01528-x

    '''
    def __init__(self, image_pts, object_pts, theta_0, pi_0):
        '''
        Initialize the calibration class.
        
        Args:
        image_pts: a list of (N_i,2) 2D image points
                    each entry in the list belongs to one image.

        object_pts: a list of (N_i,3) 3D object points
                    each entry in the list belongs to one image.
        
        theta_0: Initial intrinsic parameters for the camera. shape (k,).
        pi_0: a list of initial extrinsic parameters
                each entry in the list belongs to one image.
        '''
        self.u = image_pts # list of (N_i,2) 2d image points 
        self.X = object_pts # list of (N_i,3) 3d object points 
        # self.u[j][i]: point-i visible in jth image.
        self.theta_0 = deepcopy(theta_0) # intrinsic parameters of camera
        self.pi_0 = deepcopy(pi_0) # list of extrinsic parameters, one entry per image
        self.theta_hat = None # estimated theta
        self.pi_hat = None # estimated pi
        self.residuals = None # Residuals of the calibration
        self.J = None # Jacobian matrix


    def calibrate(self, robustify = False):
        '''
        Bundle-adjustment calibration to estimate theta_hat and pi_hat.
        Cost: ∑_j ∑_i ||u_{ij} - project(X_{ij}, theta, pi_j)||², eq. R1:(5)
        RMSE: sqrt( 1/N ∑_j ∑_i ||u_{ij} - project(X_{ij}, theta_hat, pi_hat_j)||² ), eq. R1:(6)
        '''
        params0 = np.hstack([self.theta_0] + [p.ravel() for p in self.pi_0])

        def resfun(params):
            k = self.theta_0.size
            theta = params[:k]
            pis = params[k:].reshape((len(self.pi_0), -1))
            res = [] # residual
            for j, (u_j, X_j) in enumerate(zip(self.u, self.X)): # j over images
                pi = pis[j]

                u_projected = self.project(X_j, theta, pi)
                res.append((u_j - u_projected).ravel())
            return np.hstack(res)
        
        sol = least_squares(resfun, params0, loss="huber" if robustify else "linear")
        p = sol.X
            