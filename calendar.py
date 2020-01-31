for day in days:
            # Print day
            print('{0:<3}'.format(day), end='')
            start_pos += 1
            if start_pos == 7:
                # If start_pos == 7 (Sunday) start new line
                print()
                start_pos = 0 # Reset counter
        print('\n')