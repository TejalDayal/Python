{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Interest Rate:8\n",
      "Duration: 1\n",
      "Risk: 2\n"
     ]
    }
   ],
   "source": [
    "i=float(input(\"Interest Rate:\"))\n",
    "y=float(input(\"Duration: \"))\n",
    "r=float(input(\"Risk: \"))\n",
    "if((i>=7 and i<=10) and (r>=0 and r<1) and ((y>=0 and y<1) or (y>=1 and y<2) or (y>=2 and y<=3))):\n",
    "    print(\"Investment is High\")\n",
    "if((i>=3 and i<7) and (r>=0 and r<1) and ((y>=0 and y<1) or (y>=1 and y<2) or (y>=2 and y<=3))):\n",
    "    print(\"Investment is Marginal\")\n",
    "if(((i>=3 and i<7) or (i>=7 and i<=10)) and (r>=1 and r<2) and ((y>=0 and y<1) or (y>=1 and y<2) or (y>=2 and y<=3))):\n",
    "    print(\"Investment is Low\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
