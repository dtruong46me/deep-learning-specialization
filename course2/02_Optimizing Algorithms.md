## Mini-batch Gradient Descent

**Batch vs Mini-batch Gradient Descent**
- When the sample is very large (e.g. 50,000,000 samples), so to train this data will take a huge processing time
- The 50,000,000 won't fit in the memory at once
- So we split the data into the smaller size, called **batch** (e.g. `batch_size=1000`)

- While in Mini-batch Gradient Descent, we run the GD on the mini datasets

- Pseudo code of Mini-batch Algorithm:
    ```
    for t=1: 
        AL, caches = forward_prop(X[t], Y[t])
        cost = compute_cost(AL, Y[t])
        grads = backward_prop(AL, caches)
        update_parameters(grads)
    ```

> [!NOTE]
> - Batch Gradient Descent: `batch-size=m`
>   > Too long per iteration *(epoch)*
> - Mini-batch Gradient Descent: `batch_size = k` where $k \in {8,16,32,64,128,...}$
>   > Faster learning and does not always exactly convergent
> - Stochastic Gradient Descent: `batch_size = 1s`
>   > Too noisy regarding cost minimization and can not be convergent

## RMSprop Optimization Algorithm

## Adam Optimization Algorithm

## Other Learning Rate Decay Method