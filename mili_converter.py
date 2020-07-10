{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Input             Output\n",
    "# (milliseconds)    (Calculated Time) \n",
    "# --------------    -----------------\n",
    "# 555               just 555 millisecond/s==>1000ml\n",
    "# 2001              2 second/s==>//1000\n",
    "# 60011             1 minute/s==>//1000*60\n",
    "# 122011            2 minute/s 2 second/s==>122011//60*1000==>2,2011//1000==>2\n",
    "# 3661011           1 hour/s 1 minute/s 1 second/s==>60*60*1000==>1,61011//60*1000==>1,1000//1000==>1\n",
    "# 7200011           2 hour/s\n",
    "# 7322011           2 hour/s 2 minute/s 2 second/s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": "1 hour/s 1 minute/s 1 second/s\n"
    },
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": "True"
     },
     "metadata": {},
     "execution_count": 60
    }
   ],
   "source": [
    "a='3661011'\n",
    "a=int(a)\n",
    "x=''\n",
    "if a>999:\n",
    "    while a>999:    \n",
    "            if a>3600000:\n",
    "                b,a=divmod(a,3600000)\n",
    "                x+=f'{b} hour/s'\n",
    "            elif a>60000:\n",
    "                b,a=divmod(a,60000)\n",
    "                x+=f' {b} minute/s'\n",
    "            else:\n",
    "                b,a=divmod(a,1000)\n",
    "                x+=f' {b} second/s'\n",
    "else:\n",
    "    x+=f'just {a} millisecond/s'\n",
    "print(x) \n",
    "a='123123'       \n",
    "a.isdigit()"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2-final"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python38264bit2d5236eee77a4df4ac120aaa40c7d773",
   "display_name": "Python 3.8.2 64-bit"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}