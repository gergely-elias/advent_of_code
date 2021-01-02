print(
    (
        lambda f={
            int(b): -i
            for i, b in enumerate(list(__import__("fileinput").input())[1].split(","))
            if b != "x"
        }: (
            lambda M=__import__("math").prod(f): sum(
                [v * pow(M // k, k - 1) for k, v in f.items()]
            )
            % M
        )()
    )()
)
