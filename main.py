#!/usr/bin/env python3

import hashlib
import argparse
import sys
import time
from concurrent.futures import ThreadPoolExecutor

print(r"""

=======================================================================================
  ______ .______          ___       ______  __  ___ .___  ___.      ___      .______   
 /      ||   _  \        /   \     /      ||  |/  / |   \/   |     /   \     |   _  \  
|  ,----'|  |_)  |      /  ^  \   |  ,----'|  '  /  |  \  /  |    /  ^  \    |  |_)  | 
|  |     |      /      /  /_\  \  |  |     |    <   |  |\/|  |   /  /_\  \   |   ___/  
|  `----.|  |\  \----./  _____  \ |  `----.|  .  \  |  |  |  |  /  _____  \  |  |      
 \______|| _| `._____/__/     \__\ \______||__|\__\ |__|  |__| /__/     \__\ | _|      
=======================================================================================

""")

print("[+] Welcome to CrackMap")
time.sleep(1)

args = argparse.ArgumentParser(add_help=False)
args.add_argument("-p", required=False, type=str)
args.add_argument("-w", required=False, type=str)
args.add_argument("-m", required=False, type=str)
args.add_argument("-h", required=False, action='store_true')
ex_args = args.parse_args()
target = ex_args.p
wordlist = ex_args.w
mode = ex_args.m
help1 = ex_args.h

def hash_crack():
    print("[+] Cracking:")
    with open (wordlist, "r", encoding='latin-1') as file:
        words = [word.strip() for word in file.readlines()]
    with open (target, "r") as f:
        hash1 = f.read()
    def cracking(word):
        try:
            if mode == "md5":
                hashlib.md5(word.encode()).hexdigest()
            elif mode == "sha1":
                hashlib.sha1(word.encode()).hexdigest()
            elif mode == "sha256":
                hashlib.sha256(word.encode()).hexdigest()
            elif mode == "sha512":
                hashlib.sha512(word.encode()).hexdigest()
            if word == hash1:
                print(f"[+] Password Found: {word}")
        except Exception as e:
            print(f"[-] Error: {e}")
            sys.exit()
        except KeyboardInterrupt:
            sys.exit()
    with ThreadPoolExecutor(max_workers=100) as executor:
        for w in words:
            executor.submit(cracking, w)
valid_modes = {"md5", "sha1", "sha256", "sha512"}
if mode in valid_modes:
    hash_crack()
if help1:
    print("""
    
    ===================================================================
    -m to specify mode valid modes so far are md5, sha1, sha256, sha512
    ===================================================================
    -p to specify hash, it must be in a txt file
    ===================================================================
    -w to specify wordlist
    ===================================================================
    
    """)