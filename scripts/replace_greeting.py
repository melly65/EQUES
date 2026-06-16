#!/usr/bin/env python3
"""Replace greeting text in OpenOmniBot UI"""
import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--english', required=True)
    parser.add_argument('--chinese', required=True)
    parser.add_argument('--english-sub', default='')
    parser.add_argument('--chinese-sub', default='')
    parser.add_argument('--source', required=True)
    args = parser.parse_args()

    src = args.source

    # Chat empty greeting widget
    path = os.path.join(src, 'ui/lib/features/home/pages/chat/widgets/chat_empty_greeting.dart')
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace("Hi \u270b, I'm OpenOmniBot", args.english)
        content = content.replace("\u4f60\u597d\u270b\uff0c\u6211\u662fOpenOmniBot", args.chinese)
        if args.english_sub:
            content = content.replace("I can help you", args.english_sub)
        if args.chinese_sub:
            content = content.replace("\u6211\u53ef\u4ee5\u5e2e\u52a9\u4f60", args.chinese_sub)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [OK] Updated greeting in: {path}")

    print(f"\n\u2705 Greeting replaced: EN='{args.english}' / CN='{args.chinese}'")

if __name__ == '__main__':
    main()
