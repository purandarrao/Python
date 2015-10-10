# Python
Setting environment variables using source command, set in file

sample source file:
  export username=<user_value>
  expor password=<passwd>
  ...
  ...

pass the source file to updateEnv("<source file path>")

Next execute commands that needs the environment variable from the above sourced file by calling python_execute("<cmd>")
This function returns 3 parameters viz., status, output, error for the command that was executed.


If any ideas to improve, do provide your comments in making this better.
