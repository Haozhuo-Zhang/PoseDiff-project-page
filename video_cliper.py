import cv2

def trim_videos_to_same_frames(video1_path, video2_path, output1_path, output2_path):
    # Open the videos
    cap1 = cv2.VideoCapture(video1_path)
    cap2 = cv2.VideoCapture(video2_path)

    # Get properties
    fps1 = cap1.get(cv2.CAP_PROP_FPS)
    fps2 = cap2.get(cv2.CAP_PROP_FPS)
    frames1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
    frames2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

    # Target frame count = min of both
    target_frames = min(frames1, frames2)

    # Get frame width and height
    width1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
    height1 = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
    height2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define video writers
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out1 = cv2.VideoWriter(output1_path, fourcc, fps1, (width1, height1))
    out2 = cv2.VideoWriter(output2_path, fourcc, fps2, (width2, height2))

    # Write frames
    for i in range(target_frames):
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        if not ret1 or not ret2:
            break
        out1.write(frame1)
        out2.write(frame2)

    # Release everything
    cap1.release()
    cap2.release()
    out1.release()
    out2.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    trim_videos_to_same_frames(
        "./static/videos/alpha/alpha_orig.mp4",
        "./static/videos/alpha/alpha_posediff.mp4",
        "./static/videos/alpha/alpha_orig.mp4",
        "./static/videos/alpha/alpha_posediff.mp4"
    )
