<h1> 0x0D-web_stack_debugging_0 </h1>
```markdown
# Webstack Debugging Series

## Background Context

The Webstack debugging series aims to train individuals in the art of debugging. Computers and software often do not work as expected, and debugging is an essential skill for a Full-Stack Software Engineer. Mastery of debugging requires practice.

In this series, broken or bugged webstacks will be provided, and the ultimate goal is to create a Bash script that, when executed, will restore the webstack to a working state. Before writing the Bash script, it is crucial to manually identify and fix the issues.

Let's consider a simple example. The server must:

- Have a copy of the /etc/passwd file in /tmp
- Have a file named /tmp/isworking containing the string OK

Without these two elements, the web application cannot function. The task is to fix the server.

```bash
vagrant@vagrant:~$ docker run -d -ti ubuntu:14.04
...

# Followed by the debugging steps
...

vagrant@vagrant:~$
```

If the server is fixed, the answer file would contain:

```bash
sylvain@ubuntu:~$ cat answerfile
#!/usr/bin/env bash
# Fix my server with these magic 2 lines
cp /etc/passwd /tmp/
echo OK > /tmp/isworking
sylvain@ubuntu:~$
```

Note that interactive software such as emacs or vi cannot be used in the Bash script; everything must be done from the command line, including file editing.

## Installing Docker

For this project, a container is provided for solving the task. If you want to experiment locally, you can install Docker on your machine, Ubuntu 14.04 VM, or Ubuntu 16.04 VM if you upgraded.

- [Mac OS](docker-mac-link)
- [Windows](docker-windows-link)
- [Ubuntu 14.04](docker-ubuntu-14-link) (Note: Docker for Ubuntu 14 is deprecated, and adjustments are needed)
- [Ubuntu 16.04](docker-ubuntu-16-link)

## Resources

- `man` or `help` command
- `curl` command

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All files interpreted on Ubuntu 14.04 LTS
- All files should end with a new line
- Mandatory README.md file at the root of the project folder
- All Bash script files must be executable
- Bash scripts must pass Shellcheck without any error
- Bash scripts must run without error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script does
```

This markdown file provides a formatted version of the given information for better readability.
