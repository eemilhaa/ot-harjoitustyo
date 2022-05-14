import unittest
import pygame
from loaders.image_loader import load_image
from loaders.font_loader import load_font


class TestLoaders(unittest.TestCase):
    def setUp(self):
        pygame.init()

    def test_image_loader(self):
        result = load_image("ground.png")
        self.assertTrue(type(result) == pygame.Surface)

    def test_font_loader(self):
        result = load_font("bold.ttf", 12)
        self.assertTrue(type(result) == pygame.font.Font)
