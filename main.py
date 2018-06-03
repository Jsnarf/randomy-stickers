import random

# TODO : Optimize it :)
# TODO : Add Configuration
# TODO : Add Logging


def get_one_full_album():
  stickers_to_get = range(number_of_stickers_to_get)
  iteration = 0
  number_of_packets_to_buy = 0
  usable_stickers_foreach_packet = []
  real_number_of_packets_you_should_buy = 0

  # Loop until all stickers are done
  while len(stickers_to_get) > 0:

    # Get one packet
    packet_stickers = []
    while len(packet_stickers) < 5:
      new_sticker = random.randint(0, number_of_stickers_to_get)
      if new_sticker not in packet_stickers:
        packet_stickers.append(new_sticker)

    # Calculation on the last 5 packets of how many stickers have been used
    # If their number * price for one sticker is lower than number of packets (5) * price for one packet
    # => We should not buy more stickers
    if number_of_packets_to_buy == 0:
      stickers_usable = [x for x in packet_stickers if x in stickers_to_get]
      usable_stickers_foreach_packet.append(len(stickers_usable))

      if iteration >= 3:
        usable_sticker_on_last_5 = 0
        for i in range(iteration - 4, iteration + 1, 1):
          usable_sticker_on_last_5 += usable_stickers_foreach_packet[i]
        if usable_sticker_on_last_5 * price_of_a_sticker < 5 * price_of_a_packet:
          number_of_packets_to_buy = iteration + 1

    # Remove it from list of sticker to get
    stickers_to_get = [x for x in stickers_to_get if x not in packet_stickers]

    iteration += 1

    # Calculate real number of packets you should buy according to restriction on alone stickets you could possibly buy
    if (len(stickers_to_get) <= possibly_stickers_to_buy_alone) & real_number_of_packets_you_should_buy==0:
      real_number_of_packets_you_should_buy = iteration

  return iteration, number_of_packets_to_buy, real_number_of_packets_you_should_buy


if __name__ == "__main__":

  possibly_stickers_to_buy_alone = 50
  number_of_stickers_to_get = 683
  price_of_a_packet = 0.9
  price_of_a_sticker = 0.25

  list_of_tuples = []
  list_of_packets_to_buy = []
  list_of_tries = []

  for i in range(10):
    list_of_tuples.append(get_one_full_album())

  # Calulation on tries
  list_of_tries = [x[0] for x in list_of_tuples]
  list_of_tries.sort()

  print("Lowest iteration is : ", list_of_tries[0])
  print("Biggest iteration is : ", list_of_tries[len(list_of_tries)-1])

  average_iteration = sum(list_of_tries)/float(len(list_of_tries))
  average_card_number = average_iteration*5
  print("Average iteration is : %.2f " % average_iteration)
  print("This means that you 'll need to get %.2f packets and %.2f cards before having all the 683 cards" % (average_iteration, average_card_number))
  price_with_doubles = average_iteration * price_of_a_packet
  print("It will cost you %.2f €" % price_with_doubles)

  # Calculation on packets to buy
  list_of_packets_to_buy = [x[1] for x in list_of_tuples]
  average_number_of_packets = sum(list_of_packets_to_buy)/float(len(list_of_packets_to_buy))
  average_card_number_from_packets = average_number_of_packets * 5
  average_cards_to_buy = number_of_stickers_to_get - average_card_number_from_packets
  print("Average number of packets to buy : %.2f " % average_number_of_packets)
  print("This means that you will need to buy %.2f packets so %.2f cards but buy directly %.2f cards" % (average_number_of_packets, average_card_number_from_packets, average_cards_to_buy))
  price_with_no_doubles = average_number_of_packets * price_of_a_packet + average_cards_to_buy * price_of_a_sticker
  print("It will cost you %.2f €" % price_with_no_doubles)

  # Calculation according to the fact that we cannot buy more than X cards (50)
  list_of_real_packets_you_should_buy = [x[2] for x in list_of_tuples]
  average_real_number_of_packets = sum(list_of_real_packets_you_should_buy)/float(len(list_of_real_packets_you_should_buy))
  average_real_card_number = average_real_number_of_packets * 5
  print("Average number of real packets to buy : %.2f " % average_real_number_of_packets)
  print("This means that you will need to buy %.2f packets so %.2f cards but buy directly %.2f cards" % (average_real_number_of_packets, average_real_card_number, possibly_stickers_to_buy_alone))
  price_real_with_no_doubles = average_real_number_of_packets * price_of_a_packet + possibly_stickers_to_buy_alone * price_of_a_sticker
  print("It will cost you %.2f €" % price_real_with_no_doubles)
