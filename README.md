# manifestcreator

Quickly create Munki manifests based on a CSV template.

1. Create a CSV file that contains the serial numbers for which you want to create manifests, one per line.
2. Create a manifest called Template in your Munki repo. The configuration of this manifest will be inherited by the newly created serial number manifests.
3. Run manifestcreator using the following syntax:
    ```
    ./manifestcreator.py --repo /path/to/munki_repo /path/to/serials.csv
    ```
4. Check your manifests folder to verify that the new manifests have been created successfully.

For additional help, run `./manifestcreator.py --help`.
