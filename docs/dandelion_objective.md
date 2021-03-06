Dandelion's `objective` module is mostly inherited from [Lasagne](https://github.com/Lasagne/Lasagne) except for the CTC (Connectionist Temporal Classification) objective. 

You're recommended to refer to [`Lasagne.objectives` document](http://lasagne.readthedocs.io/en/latest/modules/objectives.html) for the following objectives:

* binary_crossentropy
* categorical_crossentropy
* squared_error
* binary_hinge_loss
* multiclass_hinge_loss
* binary_accuracy
* categorical_accuracy

_______________________________________________________________________
## ctc_cost_logscale
CTC cost calculated in `log` scale. This CTC objective is written purely in Theano, so it runs on both Windows and Linux. Theano itself also has a [wrapper](http://deeplearning.net/software/theano/library/tensor/nnet/ctc.html) for Baidu's `warp-ctc` library, which requires separate install and only runs on Linux.
```python
ctc_cost_logscale(seq, sm, seq_mask=None, sm_mask=None, blank_symbol=None, align='pre')
```
* **seq**: query sequence, shape of `(L, B)`, `float32`-typed
* **sm**: score matrix, shape of `(T, C+1, B)`, `float32`-typed
* **seq_mask**: mask for query sequence, shape of `(L, B)`, `float32`-typed
* **sm_mask**: mask for score matrix, shape of `(T, B)`, `float32`-typed
* **blank_symbol**: scalar, = `C` by default
* **align**: string, {'pre'/'post'}, indicating how input samples are aligned in one batch
* **return**: negative log likelihood averaged over a batch

_______________________________________________________________________
## ctc_best_path_decode
Decode the network output scorematrix by best-path-decoding scheme.
```python
ctc_best_path_decode(Y, Y_mask=None, blank_symbol=None)
```
* **Y**: output of a network, with shape `(B, T, C+1)`
* **Y_mask**: mask of Y, with shape `(B, T)`
* **return**: result sequence of shape `(T, B`), and result sequence mask of shape `(T, B)`

_______________________________________________________________________
## ctc_CER
Calculate the character error rate (CER) given ground truth `targetseq` and CTC decoding output `resultseq`
```python
ctc_CER(resultseq, targetseq, resultseq_mask=None, targetseq_mask=None)
```
* **resultseq**: CTC decoding output, with shape `(T1, B)`
* **targetseq**: sequence ground truth, with shape `(T2, B)`
* **return**: tuple of `(CER, TE, TG)`, in which `TE` is the batch-wise total edit distance, `TG` is the batch-wise total ground truth sequence length, and `CER` equals to `TE/TG`