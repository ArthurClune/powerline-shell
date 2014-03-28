
import os

def add_aws_segment():
    aws_user = os.getenv("AWS_USER")
    if aws_user:
        bg = Color.JOBS_BG
        fg = Color.JOBS_FG
        powerline.append(' %s ' % aws_user, fg, bg)

add_aws_segment()

