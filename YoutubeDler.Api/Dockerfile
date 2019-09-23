FROM mcr.microsoft.com/dotnet/core/aspnet:2.2-stretch-slim AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/core/sdk:2.2-stretch AS build
WORKDIR /src
COPY ["YoutubeDler.Api/YoutubeDler.Api.csproj", "YoutubeDler.Api/"]
RUN dotnet restore "YoutubeDler.Api/YoutubeDler.Api.csproj"
COPY . .
WORKDIR "/src/YoutubeDler.Api"
RUN dotnet build "YoutubeDler.Api.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "YoutubeDler.Api.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "YoutubeDler.Api.dll"]