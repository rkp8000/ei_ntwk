# analyze population spiking stats

spikes = get_spikes()

mean_fr = calc_mean_fr(spikes)
print(mean_fr)

corrs = calc_corrs(spikes)
print(corrs)

