from flow import Flow
import os
import sys

test_dir = os.path.abspath(os.path.join(__file__, "../test"))
# checkpoint = os.path.abspath(os.path.join(__file__, "../checkpoints/flownet2"))
checkpoint = "flownet2"
flow = Flow(test_dir, test_dir)

skip = sys.argv[1] if len(sys.argv) > 1 else 5
input_files = filter(lambda name: os.path.isfile(os.path.join(test_dir, "color_flow", name)),
        os.listdir(os.path.join(test_dir, "color_flow")))
indices = sorted([int(os.path.splitext(name)[0].split("_")[-1]) for name in input_files])
input_frames = list(filter(lambda i: i%skip == 0, indices))
total_frames = len(input_frames)
print(input_frames)
print("processing {} frames".format(total_frames))

index_pairs = list(zip(input_frames[:-1], input_frames[1:]))
visualize = True
flow.compute_flow(index_pairs, checkpoint, visualize)
