c = get_config()  # get the config object
c.IPKernelApp.pylab = 'inline'  # in-line figure when using Matplotlib
c.NotebookApp.ip = '*'
c.NotebookApp.allow_remote_access = True # allow access from outside localhost
c.NotebookApp.open_browser = False  # do not open a browser window by default when using notebooks
c.NotebookApp.notebook_dir = '/notebooks'
c.NotebookApp.allow_root = True # Allow to run Jupyter from root user inside Docker container
