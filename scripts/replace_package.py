#!/usr/bin/env python3
"""Replace package name cn.com.omnimind.bot → br.com.melly.bot"""
import os
import sys
import argparse

def replace_in_content(filepath, old_pkg, new_pkg):
    if not os.path.exists(filepath):
        return False
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_pkg not in content:
        return False
    content = content.replace(old_pkg, new_pkg)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--old-package', required=True)
    parser.add_argument('--new-package', required=True)
    parser.add_argument('--source', required=True)
    args = parser.parse_args()

    src = args.source
    old = args.old_package
    new = args.new_package

    files = [
        'app/build.gradle.kts',
        'app/src/main/AndroidManifest.xml',
        'ui/android/app/build.gradle.kts',
        'ui/android/app/src/main/AndroidManifest.xml',
        'settings.gradle.kts',
        'build.gradle.kts',
    ]

    old_path = old.replace('.', '/')
    new_path = new.replace('.', '/')
    java_root = os.path.join(src, 'app/src/main/java')
    old_dir = os.path.join(java_root, old_path)
    new_dir = os.path.join(java_root, new_path)

    if os.path.exists(old_dir):
        os.makedirs(os.path.dirname(new_dir), exist_ok=True)
        os.rename(old_dir, new_dir)
        print(f"  [OK] Renamed: {old_dir} → {new_dir}")

    for root, dirs, filenames in os.walk(java_root):
        for fname in filenames:
            if fname.endswith(('.kt', '.java', '.kts')):
                fpath = os.path.join(root, fname)
                if replace_in_content(fpath, old, new):
                    print(f"  [OK] Package in: {fpath}")

    for f in files:
        fpath = os.path.join(src, f)
        if replace_in_content(fpath, old, new):
            print(f"  [OK] {f}")

    dart_root = os.path.join(src, 'ui/lib')
    if os.path.exists(dart_root):
        for root, dirs, filenames in os.walk(dart_root):
            for fname in filenames:
                if fname.endswith('.dart'):
                    fpath = os.path.join(root, fname)
                    if replace_in_content(fpath, old, new):
                        print(f"  [OK] Package in Dart: {fpath}")

    scripts_dir = os.path.join(src, 'scripts')
    if os.path.exists(scripts_dir):
        for root, dirs, filenames in os.walk(scripts_dir):
            for fname in filenames:
                if fname.endswith(('.sh', '.py', '.yaml', '.yml')):
                    fpath = os.path.join(root, fname)
                    if replace_in_content(fpath, old, new):
                        print(f"  [OK] Package in script: {fpath}")

    print(f"\n✅ Package renamed: {old} → {new}")

if __name__ == '__main__':
    main()
