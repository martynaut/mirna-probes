import click
from probes_helpers import search


@click.command()
@click.argument('seq')
@click.option('--org', '-o')
def main(seq, org='hsa'):
    if not org:
        org = 'hsa'

    click.echo("Probes for: {}, {}".format(seq, org))

    filename, status = search(seq1=seq, org=org)

    if status:
        click.echo("Results saved in {}".format(filename))
    else:
        click.echo("No matching sequences found")


if __name__ == "__main__":
    main()
