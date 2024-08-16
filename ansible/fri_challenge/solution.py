---
- name: Show off Ansible skillz
  hosts: working
  connection: ssh     # default is to use the connection plugin ssh.py
  gather_facts: yes   # default is yes
  become: true

  vars_prompt:
  - name: "my_color_choice"
    prompt: "What is your favorite color?"
    private: false
    default: "White"

  tasks:                               # a list of what we want to do
  - name: Create secret directory      # for part 2
    ansible.builtin.file:
      path: "/home/secret/"
      state: "directory"
      mode: "0755"

  - name: Copies a file to machines          # for part 2
    ansible.builtin.copy:
      src: ~/mycode/fri_challenge/secret.txt # parameter to state which file to copy
      dest: /home/secret/secret.txt              # parameter to state where file should go
      force: yes

  - name: Create color directory
    ansible.builtin.file:
      path: "/home/color/"
      state: "directory"
      mode: "0755"

  - name: Place fav color answer in color directory
    ansible.builtin.shell: |
      echo "{{ my_color_choice }}" > /home/color/color.txt
      ls /home
    register: verify_output

  - name: Display results  # part 3
    ansible.builtin.debug:
      msg: "{{ verify_output }}"
