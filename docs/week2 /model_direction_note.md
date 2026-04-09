# Week 2 Model Direction Note

The project uses transfer learning as the core strategy for 23-class PlantVillage classification.

Reasoning:
- the dataset is large enough to benefit from transfer learning
- pretrained ImageNet features reduce convergence time
- transfer learning is more practical than training from scratch under the available compute plan
- this supports a realistic baseline path for later engineering and deployment
