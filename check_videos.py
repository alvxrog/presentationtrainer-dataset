import os
import decord

def verify(dir):
    bad_vids = []
    for file in os.listdir(dir):
        if file.endswith('.mp4'):
            video_path = os.path.join(dir, file)
            try:
                decord.VideoReader(video_path)
            except decord._ffi.base.DECORDError:
                bad_vids.append(file)
            except Exception as e:
                print(f"Unhandled exception when processing {file}: {e}")
    return bad_vids

vid_dirs = ['pt-v1/train', 'pt-v1/val']
bad_vids = []

if __name__ == '__main__':
    print(f"Starting video checking. Current paths: {vid_dirs}")
    for dir in vid_dirs:
        print(f"Processing {dir}")
        bad_vids += verify(dir)

    if bad_vids:
        print("Bad videos found:")
        for video in bad_vids:
            print(video)
    else:
        print("All videos processed correctly")