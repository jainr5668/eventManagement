import os

cmds = [
    'npx prettier --write "**/*.ts"',
    "flake8 fastApi",
    "docker build -t fastapi -f docker/Dockerfile .",
    "docker run -d -p 4200:80 fastapi",
]
for cmd in cmds:
    os.system(cmd)
