[![codecov](https://codecov.io/gh/joencina/talkipa2me/branch/master/graph/badge.svg?token=J3LNSI2QN4)](https://codecov.io/gh/joencina/talkipa2me)
# Introduction

## Description
Talk IPA 2 me! is a Django web app to translate English text to phonetic text using the International Phonetic Alphabet (IPA).
In short, Carnegie Mellon University's phonetic dictionary was translated into standard IPA symbols and a dictionary held in
`phonetic.json` was built.
Check out the Heroku-deployed version at http://www.talkipa2.me

## Example: Shakespeare's Sonnet 27
#### English 
Ah, distinctly I remember it was in the bleak December;
And each separate dying ember wrought its ghost upon the floor.
Eagerly I wished the morrow; — vainly I had sought to borrow
From my books surcease of sorrow — sorrow for the lost Lenore —
For the rare and radiant maiden whom the angels name Lenore —
Nameless here for evermore.

#### IPA 
'ɑ, dɪst'ɪŋktli 'aɪ rɪm'ɛmbər 'ɪt w'ɑz ɪn ðə bl'ik dɪs'ɛmbər;
ənd 'itʃ s'ɛpərˌeɪt d'aɪɪŋ 'ɛmbər r'ɔt 'ɪts g'oʊst əp'ɑn ðə fl'ɔr.
'igərli 'aɪ w'ɪʃt ðə m'ɑroʊ; — v'eɪnli 'aɪ h'æd s'ɔt t'u b'ɑrˌoʊ 
frʌm m'aɪ b'ʊks sˌɜrs'is ʌv s'ɑroʊ — s'ɑroʊ f'ɔr ðə l'ɔst lən'ɔr — 
f'ɔr ðə r'ɛr ənd r'eɪdˌiənt m'eɪdən h'um ðə 'eɪnʤəlz n'eɪm lən'ɔr — 
n'eɪmləs h'ir f'ɔr 'ɛvərmˌɔr.


# Local reproduction

If you want to explore this project from your own computer, clone this repository, make a new pipenv environment and follow the steps below.
You need to have a working version of Postgres installed beforehand.

#### Create a database
Run `scripts/setup.sh` (credits to Travis Jungroth)

#### Install dependencies
    pipenv install --dev
    
#### Run
    ./manage.py runserver
    