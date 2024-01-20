<h1> 0x0B-ssh </h1>
```markdown
# Cheat Sheet for Server Basics and SSH

## What is a Server?
- **Definition**: A server is a powerful computer that provides services or resources to other computers, called clients, over a network.
- **Purpose**: Servers store and manage data, host websites, run applications, and facilitate communication between devices.

## Where Servers Usually Live?
- **Location**: Servers are often kept in data centers, which are specialized facilities designed to house and maintain multiple servers.
- **Features**: Data centers provide security, backup power, and high-speed internet connections to ensure servers operate efficiently.

## What is SSH?
- **Definition**: SSH stands for Secure Shell. It is a secure protocol used to access and manage remote servers over a network.
- **Purpose**: SSH enables secure communication and allows users to execute commands, transfer files, and perform other tasks on a remote server.

## How to Create an SSH RSA Key Pair?
1. **Open Terminal (Command Line)**: On your computer, find the terminal or command line application.
2. **Generate Key Pair**: Type `ssh-keygen -t rsa` and press Enter.
3. **Follow Prompts**: You may be prompted to specify a file location (press Enter for default), and optionally set a passphrase for extra security.

## How to Connect to a Remote Host Using an SSH RSA Key Pair?
1. **Copy Public Key**: Use `cat ~/.ssh/id_rsa.pub` to display your public key. Copy it.
2. **Paste Key on Server**: On the remote server, paste the public key into the `~/.ssh/authorized_keys` file.
3. **Connect**: In the terminal, type `ssh username@remote_host` replacing "username" and "remote_host" with your server details.

## Advantage of using #!/usr/bin/env bash instead of /bin/bash
- **Flexibility**: `#!/usr/bin/env bash` is more flexible because it searches the system's `PATH` variable for the Bash executable. This allows scripts to work on different systems without specifying the exact path to the Bash interpreter.
- **Portability**: It ensures that the script uses the Bash version found in the user's environment, enhancing compatibility across different systems.
```
