"""
  @Author       : liujianhan
  @Date         : 2020/10/31 19:24
  @Project      : DailyTinyImprovement
  @FileName     : show_gif.py
  @Description  : Placeholder
"""
import imageio
import os


def compose_gif():
    gif_imgs = []
    for pic in os.listdir('pics'):
        pic = f'{os.path.abspath(__file__)}/pics{pic}'
        gif_imgs.append(imageio.imread(pic))
    imageio.imsave('test.gif', gif_imgs, fps=1)


if __name__ == '__main__':
    compose_gif()
