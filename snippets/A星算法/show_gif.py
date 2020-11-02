"""
  @Author       : liujianhan
  @Date         : 2020/10/31 19:24
  @Project      : DailyTinyImprovement
  @FileName     : show_gif.py
  @Description  : Placeholder
"""
import os

import imageio


def compose_gif():
    gif_imgs = []
    for pic in os.listdir('pics'):
        pic = f'{os.path.abspath(".")}/pics/{pic}'
        gif_imgs.append(imageio.imread(pic))
    imageio.mimsave('test_20.gif', gif_imgs, fps=20)
    imageio.mimsave('test_30.gif', gif_imgs, fps=30)
    imageio.mimsave('test_60.gif', gif_imgs, fps=60)


if __name__ == '__main__':
    compose_gif()
