"""
  @Author       : liujianhan
  @Date         : 21/3/31 11:02
  @Project      : DailyTinyImprovement
  @FileName     : 3.1_dataloader.py
  @Description  : Placeholder
"""
import os

from PIL import Image
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms

from .lenet import LeNet

BATCH_SIZE = 10
MAX_EPOCH = 100


class RMBDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        self.label_name = {'1': 0, '100': 1}
        self.data_info = self.get_img_info(data_dir)
        self.transform = transform

    def __getitem__(self, item):
        path_img, label = self.data_info[item]
        img = Image.open(path_img).convert('RGB')

        if self.transform is not None:
            img = self.transform(img)

        return img, label

    def __len__(self):
        return len(self.data_info)

    def get_img_info(self, data_dir):
        data_info = []
        for root, dirs, _ in os.walk(data_dir):
            for sub_dir in dirs:
                img_names = os.listdir(os.path.join(root, sub_dir))
                img_names = [img for img in img_names if img.endswith('.jpg')]

                for index, img in enumerate(img_names):
                    img_path = os.path.join(root, sub_dir, img)
                    label = self.label_name[sub_dir]
                    data_info.append((img_path, label))

        return data_info


if __name__ == '__main__':
    split_dir = os.path.join('data', 'rmb_split')
    train_dir = os.path.join(split_dir, 'train')
    valid_dir = os.path.join(split_dir, 'valid')
    norm_mean = [.485, .456, .406]
    norm_std = [.229, .224, .225]

    train_transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.RandomCrop(32, padding=4),
        transforms.ToTensor(),
        transforms.Normalize(norm_mean, norm_std)
    ])

    valid_transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
        transforms.Normalize(norm_mean, norm_std)
    ])

    train_data = RMBDataset(data_dir=train_dir, transform=train_transform)
    valid_data = RMBDataset(data_dir=valid_dir, transform=valid_transform)
    # todo learn the design pattern of Dataloader
    train_loader = DataLoader(dataset=train_data, batch_size=BATCH_SIZE, shuffle=True)
    valid_loader = DataLoader(dataset=valid_data, batch_size=BATCH_SIZE)

    # model, loss, optimization todo
    net = LeNet(classes=2)
    net.initialie_weights()

    for epoch in range(MAX_EPOCH):
        loss_mean = 0.
        correct = 0.
        total = 0.
        net.train()
        for i, data in enumerate(train_loader):
            inputs, labels = data
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
