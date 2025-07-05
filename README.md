# Camera_Calibration_Error_Models
A comprehensive, open-source library for error modeling, uncertainty estimation, noise characterization, and systematic error analysis in camera calibration.

## 📖 Inspiration

**Inferring Bias and Uncertainty in Camera Calibration**  
Annika Hagemann, Moritz Knorr, Holger Janssen, Christoph Stiller  
*International Journal of Computer Vision (2022)*  
[DOI: 10.1007/s11263-021-01528-x](https://doi.org/10.1007/s11263-021-01528-x)


## 🚀 Features
✅ Each function is traceable to specific equations (e.g., `compute_bias_ratio` → Eq. 12) with consistent notation.
✅ Estimate systematic bias errors in camera intrinsics & extrinsics (Eq. 11)  
✅ Compute bias ratio (Eq. 12) to detect potential model mismatches  
✅ Detector noise estimation via robust per-board group splitting (Eq. 10)  
✅ Calculate standard covariance from the calibration Jacobian (Eq. 8)  
✅ Full nonparametric bootstrap & approximated bootstrap uncertainty estimation (Eqs. 13–15, 19–20)  
✅ Mapping error residuals and expected mapping error (EME) evaluation (Eqs. 22–24)  
✅ Modular design with direct correspondence to mathematical formulations in peer-reviewed literature  
✅ Easily extendable for distortion models, fisheye, stereo rigs, or multi-camera systems



## 📷 Applications

- Assessing calibration quality in robotics, AR/VR, autonomous driving, and SLAM
- Detecting systematic calibration errors in automated pipelines
- Comparing calibration performance across datasets, devices, or algorithms
- Research into robust and uncertainty-aware camera calibration



## 🤝 Contributing

Contributions are welcome! We’re actively seeking:

- New error models or uncertainty estimators
- Support for advanced distortion (e.g., fisheye, omnidirectional)
- Benchmarks on different calibration datasets

Open an issue or pull request to get started.



## 📜 License & Usage

The software here is released **purely for non-commercial, educational, and individual research purposes**.  
It is **not authorized** for any commercial applications or for use by companies or organizations.

