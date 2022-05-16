# Script to shorten the rendering command
# Example usage: "bash render.sh 2" (render scene 2)

manim -pql scene$1.py Scene$1
