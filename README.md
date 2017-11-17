# Approximate Cross Validation
===

**hogehoge** is a Python module for approximate cross validation used in the fiels of machine learning. 

## Description

**hogehoge** is ...


## Requirements
* numpy
* jupyter (for notebooks)

## Installation
* from sourse
```bash
git clone <<url>>
cd hogehoge
python setup.py install
```

## Usage
### logistic regression
* binomial logistic regression
```python
from mean_field_cv.logistic.acv_logit import acv_logit
from mean_field_cv.logistic.saacv_logit import saacv_logit
# TODO: add learning with Scikit-learn
LOOE_ACV, ERR_ACV = acv_logit(wV, X, Ycode)  #ACV
LOOE_SAACV, ERR_SAACV = saacv_logit(wV, X, Ycode)  #SAACV
```

* mutltinomial logistic regression
```python
from mean_field_cv.logistic.acv_mlr import acv_mlr
from mean_field_cv.logistic.saacv_mlr import saacv_mlr
# TODO: add learning with Scikit-learn
LOOE_ACV, ERR_ACV = acv_mlr(wV, X, Ycode)  #ACV
LOOE_SAACV, ERR_SAACV = saacv_mlr(wV, X, Ycode)  #SAACV
```

## Document
See <<url>> for documents of modules.