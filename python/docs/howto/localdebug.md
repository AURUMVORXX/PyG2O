## Debug with VSCode

1. Install **debugpy** module

    `pip install debugpy`
    
2. Add to your code listening to the default `5678` port with debug adapter

    ```python
    import debugpy
    debugpy.listen(5678, in_process_debug_adapter=True)
    ```
    
3. Launch your G2O Server

4. In VSCode, go to your Python script, press **F5** and select **Attach using Process ID**

    ![Screenshot](https://picloud.cc/images/97bf2c4c7821af4b32b7906ba5dbee2f.png)
    
5. Find G2O Server process and select it
    
    ![Screenshot](https://picloud.cc/images/e438291ae8fe213fb6a4ff7ea57821f0.png)
    
![Screenshot](https://picloud.cc/images/70621be4531719d40606dce7fec7a49b.png)

!!! warning
    Sometimes **debugpy** isn't terminating process even after server is closed. Keep an eye on process list while attaching, so you can terminate them manually.
    
## Debug with PDB

Python Debugger (PDB) is already implemented by default, so you can place breakpoints right away

```python
@g2o.event('onTime')
def evtTime(**kwargs):
    a = 5
    b = 246
    c = a * b
    
    breakpoint()
    
    print(kwargs)
```

That way PDB interface will show up on breakpoint encounter, and you can use it [as usual](https://docs.python.org/3/library/pdb.html)

![Screenshot](https://picloud.cc/images/982c6932a818efb657406a9f4041067a.png)