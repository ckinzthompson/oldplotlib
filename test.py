if __name__ == '__main__':
	# import matplotlib.pyplot as plt
	# plt.style.use('./oldplotlib.mplstyle')
	import oldplotlib as plt
	import numpy as np
	from scipy.optimize import newton

	fig,ax = plt.subplots(2)

	## top plot
	c = 0.
	l = 20.
	lam = .01

	r = np.linspace(0,1.,1000)
	alpha_r = r*l*lam**r / (1.-r) - 1.
	y_r = alpha_r/(1. + alpha_r + l * lam**r )

	cut_low = np.nonzero(np.bitwise_and(alpha_r<1,r<.4))[0][-1]
	cut_high = np.nonzero(np.bitwise_and(alpha_r>1,r>.6))[0][0]
	ax[0].plot([1.,1.],[y_r[cut_low],r[cut_high]],lw=1.)

	ax[0].plot(alpha_r[:cut_low],r[:cut_low],linestyle='-') ## pre
	ax[0].plot(alpha_r[cut_low:cut_high],r[cut_low:cut_high],linestyle='--') ## transition
	ax[0].plot(alpha_r[cut_high:],r[cut_high:],linestyle='-') ## post

	ax[0].plot(alpha_r[:cut_low],y_r[:cut_low],linestyle='-') ## pre
	ax[0].plot(alpha_r[cut_low:cut_high],y_r[cut_low:cut_high],linestyle='--') ## transition
	ax[0].plot(alpha_r[cut_high:],y_r[cut_high:],linestyle='-') ## post

	ax[0].annotate('State and binding functions',(2.15,.32),xycoords='data')
	ax[0].annotate('when $\ell$ = %d, c = %d, $\Lambda$ = %0.2f'%(l,c,lam),(2.15,.175),xycoords='data')
	ax[0].annotate(r'$\langle$r$\rangle$',(1.1,.89),xycoords='data')
	ax[0].annotate(r'$\langle$y$\rangle$',(1.66,.63),xycoords='data')

	## bottom plot
	c = 0.
	l = 10.
	lam = .02

	r = np.linspace(0,1.,1000)
	alpha_r = r*l*lam**r / (1.-r) - 1.
	y_r = alpha_r/(1. + alpha_r + l * lam**r )

	ax[1].plot(alpha_r,r,linestyle='-')
	ax[1].plot(alpha_r,y_r,linestyle='-')

	ax[1].annotate('State and binding functions',(2.15,.32),xycoords='data')
	ax[1].annotate('when $\ell$ = %d, c = %d, $\Lambda$ = %0.2f'%(l,c,lam),(2.15,.175),xycoords='data')
	ax[1].annotate(r'$\langle$r$\rangle$',(0.31,.76),xycoords='data')
	ax[1].annotate(r'$\langle$y$\rangle$',(1.15,.56),xycoords='data')


	## fix axes
	for aa in ax:
		aa.set_xticks((0,1,2,3,4,5))
		aa.set_xlim(-.0175,5)
		aa.set_ylim(0.,1.)
		aa.set_yticks([0,.5,1.])

	ax[0].set_xticklabels(())
	ax[1].set_xlabel(r'$\alpha$')

	#### very custom figure matching fixes
	for aa in ax:
		xticks = aa.xaxis.get_major_ticks()
		xticks[0].tick1line.set_visible(False)
		xticks[0].tick2line.set_visible(False)

	ax[0].yaxis.get_major_ticks()[0].label1.set_verticalalignment('bottom')
	ax[1].yaxis.get_major_ticks()[-1].label1.set_verticalalignment('top')

	# #### Why doesn't this change the text? it changes the color!
	# for aa in ax:
	# 	yticks = aa.yaxis.get_major_ticks()
	# 	yticks[0].label1.set(text='red',color='r')
	# 	plt.show()


	######
	fig.savefig('images/test.pdf')
	plt.show()
