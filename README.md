# md5_simple_brute_force

This repository documents my problem-solving process while working on a Codewars challenge involving MD5 hash cracking using brute force.

The goal of the challenge is to recover a 5-digit numeric PIN (as a string) from a given MD5 hash.

## Problem Overview
- Given an MD5 hash representing a 5-digit PIN
- The PIN may contain leading zeros (e.g. "00011")
- The task is to determine the original plaintext PIN

Challenge reference:
https://www.codewars.com/kata/5efae11e2d12df00331f91a6

## Key Challenges
1. Handling fixed-length numeric strings with leading zeros
2. Avoiding loss of information when converting between integers and strings
3. Brute-forcing all possible 5-digit combinations efficiently

## Approach
- Iterate through all possible numeric values
- Increment values as integers for simplicity
- Convert back to a zero-padded string to preserve the correct format
- Hash each candidate using Python's `hashlib` and compare results

## What I Learned
- The importance of data representation in cryptographic problems
- Why integers and strings are not interchangeable in hashing
- How brute-force techniques work in practice and their limitations
