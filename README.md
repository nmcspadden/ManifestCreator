# manifestcreator

A tool that allows Munki administrators to quickly create manifests based on a CSV containing serial numbers.

1. Create a template manifest.

    This manifest should contain all the keys that will be _shared_ by the new serial number manifests you create. For example, you may want to include appropriate values for the `catalogs` and `included_manifests` keys.

1. Create a CSV file with serial numbers.

    The CSV file should contain a header row. The first (and possibly only) field in the header row should be `serial`. For example:

    ```
    serial
    ABCDEF10001
    ABCDEF10002
    ABCDEF10003
    ```

    The header row can contain additional comma-seperated fields, which will be used to create additional keys in the resulting manifests. For example:

    ```
    serial,display_name,user
    ABCDEF10001,"Loaner MacBook Pro",itservices
    ABCDEF10002,"Nick's iMac",nick
    ABCDEF10003,"Elliot's Mac Mini",elliot
    ```

1. Run `manifestcreator`:

    ```
    ./manifestcreator.py --repo /path/to/munki_repo /path/to/serials.csv
    ```

    :warning: `manifestcreator` will overwrite existing manifests with the same name as the newly created manifests.

1. Check your manifests folder to verify that the new manifests have been created successfully.
