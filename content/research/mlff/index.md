---
title: "Machine-learning force fields"
showDate: false
layout: simple
tags: ["Research", "Machine Learning"]
---

## Many-body gradient-domain machine learning

Atomistic insight is fundamental for computational predictive studies of chemical and physical processes.
Machine learning force fields provide a route to high-level ab initio calculations at a fraction of the cost.
[Gradient-domain machine learning][sgdml] (GDML), a kernel-based method, directly learns the relationship between atomic coordinates and interatomic forces.
However, training in the gradient domain sacrifices generalized transferability to other species or number of atoms.

Many-body GDML (mbGDML), is a technique for GDML transferability to n-sized systems by using many-body machine learning models.
Every aspect of the process from preparing quantum chemistry calculations, data set creation, training, and use of mbGDML force fields is taken care of in this [user-friendly Python package][mbgdml].

### Relevant outputs

-   [pub007 - Modeling molecular ensembles with gradient-domain machine learning force fields](../../outputs/pub007)

[sgdml]: http://quantum-machine.org/gdml/
[mbgdml]: https://github.com/keithgroup/mbGDML
